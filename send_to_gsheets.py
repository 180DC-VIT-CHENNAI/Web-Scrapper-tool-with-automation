import json
import gspread
from google.oauth2.service_account import Credentials

def sheet_id_load():
    # Here we load settings json safely and extract the sheet ID. Place Google sheet ID in the Settings.json accordingly.
    with open("settings.json", 'r', encoding='utf-8') as settings_file:
        settings = json.load(settings_file)
        return settings["sheet_id"]


def core_operations():
    # Path to your credentials file
    CREDENTIALS_FILE = 'credentials.json'

    # Define the scope
    SCOPES = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
    try: 
        SHEET_ID = sheet_id_load()
    except:
        return "Error: Settings did not load properly, thus Sheet_ID variable was not set. \nGracefully exiting..."

    # Authenticate and connect to Google Sheets
    try:
        creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
    except:
        return "Error: Credentials did not load properly, maybe credentials.json was not found. \nGracefully exiting..."
    
    try:
        gc = gspread.authorize(creds)
    except:
        return "Unable to authenticate with Google Sheets. Check if your credentials for the service account are correct."

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

    return "success"

def main():
    core_op_out = core_operations()
    if (core_op_out == "success"):
        print("Data sent to Google Sheets successfully!")
        return "success"
    else:
        print(core_op_out)
        return core_op_out