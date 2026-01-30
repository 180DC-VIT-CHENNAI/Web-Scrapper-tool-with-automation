
import fs from "fs";
import { chromium } from "playwright";
import { wrap, configure } from "agentql";
import dotenv from "dotenv";
dotenv.config();

// Get URL from command-line arguments
const url = process.argv[2];

async function scraper() {
  configure({
    apiKey: process.env.AGENTQL_API_KEY, 
  });

  const browser = await chromium.launch({ headless: true });
  const page = await wrap(await browser.newPage());

  if (!url) {
    console.error("No URL provided. Please pass a URL as a command-line argument.");
    await browser.close();
    process.exit(1);
  }

  await page.goto(url);
  await page.waitForTimeout(2000);

  // Extract description (from meta tag or first paragraph)
  let description = await page.evaluate(() => {
    const metaDesc = document.querySelector('meta[name="description"]');
    if (metaDesc && metaDesc.content) return metaDesc.content.trim();
    const firstP = document.querySelector('p');
    if (firstP) return firstP.innerText.replace(/\s+/g, ' ').trim();
    return '';
  });


  // Extract mail, phone, and social media links
  const linkDomains = {
    mail: 'mailto:',
    phone: 'tel:',
    instagram: 'instagram.com',
    linkedin: 'linkedin.com',
    twitter: 'twitter.com',
    github: 'github.com'
  };

  const extractedLinks = await page.evaluate((domains) => {
    const links = Array.from(document.querySelectorAll('a'));
    const result = {};
    for (const [key, domain] of Object.entries(domains)) {
      const found = links.find(a => a.href && a.href.toLowerCase().includes(domain));
      result[key] = found ? found.href : '';
    }
    return result;
  }, linkDomains);

  // Prepare final output in the required order
  const finalOutput = {
    description,
    extracted_links: [
      extractedLinks.mail,
      extractedLinks.phone,
      extractedLinks.instagram,
      extractedLinks.linkedin,
      extractedLinks.twitter,
      extractedLinks.github
    ]
  };

  console.log(finalOutput);
  fs.writeFileSync("data.json", JSON.stringify(finalOutput, null, 2));

  await browser.close();
}

scraper();
  