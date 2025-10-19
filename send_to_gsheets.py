import json
import gspread
from google.oauth2.service_account import Credentials

# Path to your credentials file
CREDENTIALS_FILE = 'credentials.json'
# Name of your Google Sheet
SHEET_ID = '1lCAwR_V3D-dthOaVQXyfS95DG8aDhBu4l44Z_26BDbk'  # Replace with your actual Sheet ID

# Define the scope
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# Authenticate and connect to Google Sheets
creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
gc = gspread.authorize(creds)

# Open the Google Sheet
sh = gc.open_by_key(SHEET_ID)
worksheet = sh.sheet1

# Read data from data.json
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Prepare the row to match the sheet columns
def get_link(links, key):
    for link in links:
        if isinstance(link, dict) and link.get('type') and key.lower() in link['type'].lower():
            return link.get('url', '')
        elif isinstance(link, str) and key.lower() in link.lower():
            return link
    return ''


links = data.get('extracted_links', [])
row = [
    data.get('description', ''),  # Name of Org
    get_link(links, 'instagram'),
    get_link(links, 'linkedin'),
    get_link(links, 'twitter'),
    get_link(links, 'github')
]

# Insert the row into the sheet
worksheet.append_row(row)

print('Data sent to Google Sheets successfully!')
