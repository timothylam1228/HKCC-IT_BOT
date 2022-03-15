# coding=UTF-8

import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler,  PreCheckoutQueryHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, LabeledPrice, ParseMode
from telegram.utils import helpers
from telegram.utils.helpers import escape_markdown
import os
import psycopg2
import json
from uuid import uuid4
import csv
from botocore.config import Config
import html.entities as entity

from commands.init import *


PORT = int(os.environ.get('PORT', 5000))
SO_COOL = 'hkcc-it'
FIRST, SECOND = range(2)


# Enable logging

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text(
        '/source for Geting the source\n/canteen to show canteen ')


def button(update, context):
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    query.edit_message_text(text="Selected option: {}".format(query.data))
    path = "https://github.com/timothylam1228/telegram_bot/raw/master/source/"
    file = str(query.data)
    pdf = ".pdf"
    jpg = ".jpg"
    context.bot.sendDocument(
        chat_id=query.message.chat.id, document=path+file+pdf)
    if(file == "Maths Diagnostic Test"):
        context.bot.sendPhoto(chat_id=query.message.chat.id,
                              photo='https://github.com/timothylam1228/telegram_bot/raw/master/source/maths_diagonositc_test_changed.jpg')
        context.bot.sendMessage(
            chat_id=query.message.chat.id, text=" Q7.6 has update Please be careful")


def source(update, context):
    keyboard = [
        [InlineKeyboardButton("Calculus Final Reminder",
                              callback_data='Calculus Final Reminder')],
        [InlineKeyboardButton("Calculus and Linear Final Review",
                              callback_data='Calculus and Linear Final Review')],
        [InlineKeyboardButton(
            "Calculus review", callback_data='Calculus review')],
        [InlineKeyboardButton("Calculus_Ch1_exercise",
                              callback_data='Calculus_Ch1_exercise')],
        [InlineKeyboardButton("Maths Diagnostic Test",
                              callback_data='Maths Diagnostic Test')],
        [InlineKeyboardButton("Module 1 and 2 exercise",
                              callback_data='Module 1 and 2 exercise')],
        [InlineKeyboardButton("Applied Computing", callback_data='Applied Computing'),
         InlineKeyboardButton("Programming Final Reminder", callback_data='Programming Final Reminder')],
        [InlineKeyboardButton("Stat", callback_data='Stat'),
         InlineKeyboardButton("CCT", callback_data='CCT')], [InlineKeyboardButton("Linear Final Reminder", callback_data='Linear Final Reminder')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)


def showlocation(update, context):
    chat_id = update.message.chat.id
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    dbCursor = conn.cursor()
    sqlSelect = "select * from canteen where name = '{}'".format(
        update.message.text)
    dbCursor.execute(sqlSelect)
    rows = dbCursor.fetchall()
    latitude = ""
    longitude = ""
    name = ""
    for row in rows:
        latitude = row[1]
        longitude = row[2]
        name = row[3]
    if(name != ""):
        print(name)
        context.bot.sendLocation(chat_id=chat_id, latitude=latitude,
                                 longitude=longitude, reply_markup=ReplyKeyboardRemove())


def addcanteen(update, context):
    chat_id = update.message.chat.id
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    dbCursor = conn.cursor()
    print(context.args[0])
    try:
        name = context.args[0]
        latitude = context.args[1]
        longitude = context.args[2]
        print(name)
        print(latitude)
        print(longitude)
    except:
        print("Error")

    sqlInsertTable = "INSERT INTO canteen (lat,long,name) values ({},{},'{}')".format(
        latitude, longitude, name)
    print(sqlInsertTable)
    dbCursor.execute(sqlInsertTable)
    conn.commit()
    dbCursor.close()
    conn.close()


def username(update, context):
    username = context.args[0]
    chat_id = update.message.chat.id
    context.bot.sendMessage(chat_id=chat_id, text=username)


def important_date(update, context):
    chat_id = update.message.chat.id
    f = open('date.json',)
    data = json.load(f)
    print(data)
    tmptext = ''
    for i in data['ImportantDate']:
        tmptext = tmptext+i['date']+'\n'+i['descrition']+'\n\n'
    context.bot.sendMessage(chat_id=chat_id, text=tmptext)


# @run_async

# random cat


def main():
    global update_id
    TOKEN = os.environ['TOKEN']
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # In source.py
    dp.add_handler(CommandHandler("Source", source, filters=~Filters.group))
    dp.add_handler(CommandHandler("start", start, filters=~Filters.group))
    dp.add_handler(CommandHandler("openbot", open_bot, filters=Filters.group))
    dp.add_handler(CommandHandler("openday", open_day))
    dp.add_handler(CommandHandler("endday", end_day))
    dp.add_handler(CommandHandler("gpaday", gpa_day))
    dp.add_handler(CommandHandler("date", important_date))
    dp.add_handler(CommandHandler("checkTemp", checkTemp))
    dp.add_handler(CommandHandler("wantCat", random_cat))
    dp.add_handler(CommandHandler("samgor", samgor, pass_args=True))
    # updater.dispatcher.add_handler(CallbackQueryHandler(button))
    dp.add_handler(CommandHandler("Source", source, filters=~Filters.group))
    dp.add_handler(MessageHandler(
        Filters.status_update.new_chat_members, newmember))

    # dp.add_handler(CommandHandler("lecturer",lecturer,filters=~Filters.group))
    # updater.dispatcher.add_handler(CallbackQueryHandler(rating))

    ############
    dp.add_handler(CommandHandler("addcanteen", addcanteen, pass_args=True))
    dp.add_handler(CommandHandler("username", username, pass_args=True))

    dp.add_handler(CommandHandler("ocampfee", payment, pass_args=True))
    dp.add_handler(MessageHandler(
        Filters.successful_payment, successful_payment_callback))
    dp.add_handler(PreCheckoutQueryHandler(precheckout_callback))
    dp.add_handler(CommandHandler(
        "canteen", listCanteen, filters=~Filters.group))
    dp.add_handler(CommandHandler("pin9", pin9, filters=Filters.group))
    dp.add_handler(CommandHandler("ocamp_details",
                   ocampdetail, filters=Filters.group))

    dp.add_handler(CommandHandler("week", week, filters=Filters.group))

    dp.add_handler(CommandHandler("exam", exam, pass_args=True))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.group, showlocation))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook(
        'https://serene-depths-59599.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()


'''
openbot - open the bot
openday - remaining time b4 hell
endday - remaining time to leave hell
gpaday - most excited day
pin9 - show pin message
exam - exam {code} show exam date time
week - new is week ?
'''
