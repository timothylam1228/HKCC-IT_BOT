from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.utils import helpers
SO_COOL = 'hkcc-it'
import psycopg2
import os
import time
def get_message_ids(update, context):
    message = update.message.message_id
    print('message',message)
