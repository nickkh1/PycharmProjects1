# import os
# import logging
# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
#
# from google.oauth2 import service_account
# from googleapiclient.discovery import build
#
# # Set up logging
# logging.basicConfig(level=logging.INFO)
#
# # Telegram API token
# TELEGRAM_API_TOKEN = "6110659880:AAERdttKJ-vCuGO0jf1CjpbnU2xTyWNjSKs"
#
# # Google Sheets API settings
# GOOGLE_SHEETS_API_SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
# GOOGLE_SHEETS_API_CREDENTIALS_FILE = "C:/Users/nick-/Desktop/TG_test/splendid-sunset-381417-350e9c1cc34e.json"
# GOOGLE_SHEETS_SPREADSHEET_ID = "1m0pvR_7nSk1_MqoCe3yvJvBcr-bWvbll-y5x9JeAs60"
#
# # Create a Google Sheets API client
# credentials = service_account.Credentials.from_service_account_file(GOOGLE_SHEETS_API_CREDENTIALS_FILE, scopes=GOOGLE_SHEETS_API_SCOPES)
# sheets_api = build('sheets', 'v4', credentials=credentials)
#
#
# def start(update: Update, context: CallbackContext):
#     update.message.reply_text("Welcome! Please type the niche you're interested in, and I'll provide you with information from our database.")
#
#
# def get_niche_info(niche):
#     sheet_name = "Лист1"  # Replace with your sheet name
#     range_name = f"{sheet_name}!A1:RO34"  # Adjust the range according to your sheet
#
#     result = sheets_api.spreadsheets().values().get(spreadsheetId=GOOGLE_SHEETS_SPREADSHEET_ID, range=range_name).execute()
#     rows = result.get('values', [])
#
#     for row in rows:
#         if row and row[0].lower() == niche.lower():
#             return row[1:]
#     return None
#
# def handle_message(update: Update, context: CallbackContext):
#     niche = update.message.text
#     info = get_niche_info(niche)
#
#     if info:
#         update.message.reply_text(f"Here's the information for the niche '{niche}':\n{', '.join(info)}")
#     else:
#         update.message.reply_text(
#             f"Sorry, we couldn't find any information for the niche '{niche}' in our database.")
#
# def main():
#     # Set up the Telegram bot
#     from telegram.ext import Queue
#     update_queue = Queue()
#     updater = Updater(TELEGRAM_API_TOKEN, update_queue=update_queue)
#     dispatcher = updater.dispatcher
#
#     # Add handlers
#     dispatcher.add_handler(CommandHandler("start", start))
#     dispatcher.add_handler(MessageHandler(filters.text & ~filters.command, handle_message))
#
#     # Start the bot
#     updater.start_polling()
#     updater.idle()
#
# if __name__ == "__main__":
#     main()

# This code completes the implementation of the Telegram bot. Replace YOUR_TELEGRAM_API_TOKEN with the token you received from BotFather, and replace path/to/your/credentials.json with the path to the JSON key file you downloaded from the Google Cloud Console. Replace YOUR_SPREADSHEET_ID with the ID of the Google Sheet you want to use as your database.

# Run the script using:
# python telegram_bot.py


# we are the owners of business that helps wildberries sellers in russia to find new niches to start selling on the marketplace.
# please help me to create a bot in telegram via python where user can type a particular niche and then the info about this niche is provided to him from database in googlesheet


# Новый, под который не установлена библиотека
# import os
# import telebot
# from google.oauth2 import service_account
# from googleapiclient.discovery import build
#
# # Telegram API token
# TELEGRAM_API_TOKEN = "YOUR_TELEGRAM_API_TOKEN"
#
# # Google Sheets API settings
# GOOGLE_SHEETS_API_SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
# GOOGLE_SHEETS_API_CREDENTIALS_FILE = "path/to/your/credentials.json"
# GOOGLE_SHEETS_SPREADSHEET_ID = "YOUR_SPREADSHEET_ID"
#
# # Create a Google Sheets API client
# credentials = service_account.Credentials.from_service_account_file(GOOGLE_SHEETS_API_CREDENTIALS_FILE,
#                                                                     scopes=GOOGLE_SHEETS_API_SCOPES)
# sheets_api = build('sheets', 'v4', credentials=credentials)
#
# # Initialize the telebot
# bot = telebot.TeleBot(TELEGRAM_API_TOKEN)
#
#
# def get_niche_info(niche):
#     sheet_name = "Sheet1"  # Replace with your sheet name
#     range_name = f"{sheet_name}!A1:Z"  # Adjust the range according to your sheet
#
#     result = sheets_api.spreadsheets().values().get(spreadsheetId=GOOGLE_SHEETS_SPREADSHEET_ID,
#                                                     range=range_name).execute()
#     rows = result.get('values', [])
#
#     for row in rows:
#         if row and row[0].lower() == niche.lower():
#             return row[1:]
#     return None
#
#
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.reply_to(message,
#                  "Welcome! Please type the niche you're interested in, and I'll provide you with information from our database.")
#
#
# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     niche = message.text
#     info = get_niche_info(niche)
#
#     if info:
#         bot.reply_to(message, f"Here's the information for the niche '{niche}':\n{', '.join(info)}")
#     else:
#         bot.reply_to(message, f"Sorry, we couldn't find any information for the niche '{niche}' in our database.")
#
#
# if __name__ == "__main__":
#     bot.polling()





'''еще один'''

import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from aiogram.utils import executor
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Telegram API token
TELEGRAM_API_TOKEN = "YOUR_TELEGRAM_API_TOKEN"

# Google Sheets API settings
GOOGLE_SHEETS_API_SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
GOOGLE_SHEETS_API_CREDENTIALS_FILE = "path/to/your/credentials.json"
GOOGLE_SHEETS_SPREADSHEET_ID = "YOUR_SPREADSHEET_ID"

# Create a Google Sheets API client
credentials = service_account.Credentials.from_service_account_file(GOOGLE_SHEETS_API_CREDENTIALS_FILE,
                                                                    scopes=GOOGLE_SHEETS_API_SCOPES)
sheets_api = build('sheets', 'v4', credentials=credentials)

# Initialize the aiogram
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TELEGRAM_API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


def get_niche_info(niche):
    sheet_name = "Sheet1"  # Replace with your sheet name
    range_name = f"{sheet_name}!A1:Z"  # Adjust the range according to your sheet

    result = sheets_api.spreadsheets().values().get(spreadsheetId=GOOGLE_SHEETS_SPREADSHEET_ID,
                                                    range=range_name).execute()
    rows = result.get('values', [])

    for row in rows:
        if row and row[0].lower() == niche.lower():
            return row[1:]
    return None


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(
        "Welcome! Please type the niche you're interested in, and I'll provide you with information from our database.")


@dp.message_handler()
async def handle_message(message: types.Message):
    niche = message.text
    info = get_niche_info(niche)

    if info:
        await message.reply(f"Here's the information for the niche '{niche}':\n{', '.join(info)}")
    else:
        await message.reply(f"Sorry, we couldn't find any information for the niche '{niche}' in our database.")


if __name__ == "__main__":
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
