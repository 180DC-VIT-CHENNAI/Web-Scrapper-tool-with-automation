# Web-Scrapper-tool-with-automation

[![Build and Push n8n Image with defaults to GHCR.io](https://github.com/SugeethJSA/Web-Scrapper-tool-with-automation/actions/workflows/npm-publish-github-packages.yml/badge.svg?branch=main)](https://github.com/SugeethJSA/Web-Scrapper-tool-with-automation/actions/workflows/npm-publish-github-packages.yml)

## Introduction

This is a one of the 180 Degrees Consulting - VIT Chennai Technical team's sample projects to showcase their work. It's an interesting project where we take a website and scrape the data off it. This web scrapper is configured to extract mail, phone number, and popular social media links from the webpage, with the help of AI too. It is a **web scraping + automation pipeline** that extracts structured information from websites and automatically pushes it to **Google Sheets**, with a **Streamlit UI** for ease of use; and allows for integration with n8n automation.

## 🚀 Features

- 🌐 Intelligent web scraping using **Playwright + AgentQL**
- 🧠 Non‑fragile extraction (no hard‑coded selectors)
- 🖥️ Streamlit‑based GUI (no CLI required)
- 📄 Structured JSON output
- 📊 Automatic Google Sheets integration
- 🔐 Secure secrets handling (`.env`, service accounts)
- 🐳 Docker support for reproducible builds

## Documentation

Visit the website below to take a look at the documentation for the project. Website: [https://sugeeth.craft.me/180DC/vitc/web-scrapper](https://sugeeth.craft.me/180DC/vitc/web-scrapper)

## ⚙️ Prerequisites

- Node.js **v18+**
- Python **3.9+**
- Google Cloud Project with Sheets API enabled
- AgentQL API key

## 🧱 Tech Stack

| **Layer**  | **Technology**       |
| ---------- | -------------------- |
| Frontend   | Streamlit (Python)   |
| Scraper    | Node.js + Playwright |
| AI Layer   | AgentQL              |
| Automation | Python               |
| Output     | Google Sheets        |
| Deployment | Docker               |

## 📁 Project Structure

```other
Web-Scrapper-tool-with-automation/
│
├── main.py                 # Streamlit UI
├── scrapper.js             # Playwright + AgentQL scraper
├── send_to_gsheets.py      # Google Sheets automation
├── data.json               # Scraped output (auto‑generated)
├── requirements.txt        # Python dependencies
├── docker-compose.yml      # Docker orchestration
├── .env                    # API keys
├── credentials.json        # Google service account (required)
├── README.md
├── settings.json           # Storing Sheet_ID among others
└── .gitignore
```

## Running Modes
- It can run using the Streamlit interface on laptops.
- Or for server-side deployments, you can invoke and process the files via the command line interface too. We have a sample n8n automation docker package that you can download and check out to use the scrapper.

It's currently up for review. If anyone is interested, please review the code and/or documentation and provide suggestions. I'd be happy to receive feedback and learn.

Thank you everyone for your kind support in helping to make this possible.
