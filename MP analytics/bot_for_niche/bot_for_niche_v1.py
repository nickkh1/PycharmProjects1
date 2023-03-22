import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from google.oauth2 import service_account
from googleapiclient.discovery import build

# Set up logging
logging.basicConfig(level=logging.INFO)

# Telegram API token
TELEGRAM_API_TOKEN = "YOUR_TELEGRAM_API_TOKEN"

# Google Sheets API settings
GOOGLE_SHEETS_API_SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
GOOGLE_SHEETS_API_CREDENTIALS_FILE = "path/to/your/credentials.json"
GOOGLE_SHEETS_SPREADSHEET_ID = "YOUR_SPREADSHEET_ID"

# Create a Google Sheets API client
credentials = service_account.Credentials.from_service_account_file(GOOGLE_SHEETS_API_CREDENTIALS_FILE, scopes=GOOGLE_SHEETS_API_SCOPES)
sheets_api = build('sheets', 'v4', credentials=credentials)


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome! Please type the niche you're interested in, and I'll provide you with information from our database.")


def get_niche_info(niche):
    sheet_name = "Sheet1"  # Replace with your sheet name
    range_name = f"{sheet_name}!A1:Z"  # Adjust the range according to your sheet

    result = sheets_api.spreadsheets().values().get(spreadsheetId=GOOGLE_SHEETS_SPREADSHEET_ID, range=range_name).execute()
    rows = result.get('values', [])

    for row in rows:
        if row and row[0].lower() == niche.lower():
            return row[1:]
    return None

def handle_message(update: Update, context: CallbackContext):
    niche = update.message.text
    info = get_niche_info(niche)

    if info:
        update.message.reply_text(f"Here's the information for the niche '{niche}':\n{', '.join(info)}")
    else:
        update.message.reply_text(
            f"Sorry, we couldn't find any information for the niche '{niche}' in our database.")

def main():
    # Set up the Telegram bot
    updater = Updater(TELEGRAM_API_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Add handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

