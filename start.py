#coding=UTF-8

import logging
import boto3
from botocore.exceptions import ClientError
import random
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler,StringCommandHandler, InlineQueryHandler
from telegram import InlineQuery , ReplyKeyboardMarkup, ReplyKeyboardRemove, MessageEntity, ForceReply, InlineKeyboardButton,InlineKeyboardMarkup,InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent, LabeledPrice
from telegram.utils import helpers
from telegram.utils.helpers import escape_markdown
import requests
from xml.etree import ElementTree
import os
from datetime import datetime
import psycopg2
import json
from uuid import uuid4
import csv
import cv2
import numpy as np
from botocore.config import Config
from io import BytesIO
import tempfile
from PIL import Image

PORT = int(os.environ.get('PORT', 5000))
SO_COOL = 'hkcc-it'
FIRST, SECOND = range(2)
# s3 =boto3.resource('s3',
#  aws_access_key_id='AKIAUVVDLOIF5VTRKBQH',
#     aws_secret_access_key="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")
# bucket = s3.Bucket('telegram.bot.web')
# client = boto3.client(
#     's3',
#     aws_access_key_id='AKIAUVVDLOIF5VTRKBQH',
#     aws_secret_access_key="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"
# )


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('/source for Geting the source\n/canteen to show canteen')

def newmember(update, context):
    """Send a message when the command /help is issued."""
    query = update.callback_query
    bot = context.bot
    url = helpers.create_deep_linked_url(bot.get_me().username, SO_COOL)
    text = "歡迎來到IT谷"
    keyboard = InlineKeyboardMarkup.from_button(
        InlineKeyboardButton(text='Continue here!', url=url)
        )
    ogg_url = 'https://github.com/timothylam1228/CodeDeployGitHubDemo/raw/master/source/plato.ogg'
    for member in update.message.new_chat_members:
        update.message.reply_text(text, reply_markup=keyboard)
        context.bot.send_voice(chat_id = update.message.chat.id, voice = ogg_url)
        new_members = update.message.new_chat_members
        firstname = member.first_name
        lastname = member.last_name
        if("+852" in firstname) :
            bot.kick_chat_member(chat_id=update.message.chat.id, user_id=update.message.from_user.id)
            return
        elif("+852" in lastname):
            bot.kick_chat_member(chat_id=update.message.chat.id, user_id=update.message.from_user.id)
            return



def open_bot(update, context):
    x = update.message.from_user.id
    print(x)
    bot = context.bot
    url = helpers.create_deep_linked_url(bot.get_me().username, SO_COOL)
    keyboard = InlineKeyboardMarkup.from_button(
        InlineKeyboardButton(text='Get Resource here!', url=url)
    )
    #context.bot.sendMessage(chat_id=update.message.chat.id,text ="        Hello",reply_markup=keyboard)
    update.message.reply_text("Hello", reply_markup=keyboard)


def button(update, context):
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    query.edit_message_text(text="Selected option: {}".format(query.data))
    path="https://github.com/timothylam1228/telegram_bot/raw/master/source/"
    file=str(query.data)
    pdf=".pdf"
    jpg=".jpg"
    context.bot.sendDocument(chat_id=query.message.chat.id, document=path+file+pdf)
    if(file=="Maths Diagnostic Test"):
        context.bot.sendPhoto(chat_id=query.message.chat.id, photo='https://github.com/timothylam1228/telegram_bot/raw/master/source/maths_diagonositc_test_changed.jpg')
        context.bot.sendMessage(chat_id=query.message.chat.id,text =" Q7.6 has update Please be careful")


def open_day(update, context):
    x = datetime.datetime.now()
    delta = datetime.datetime(2021, 1, 25) - datetime.datetime.now()
    count = (delta.total_seconds())
    days = int(count//86400)
    hours = int((count-days*86400)//3600)
    minutes = int((count-days*86400-hours*3600)//60)
    seconds = int(count-days*86400-hours*3600-minutes*60)
    #update.message.reply_text("開左學啦仲倒數 \n用 /endday 睇下幾時完SEM",reply_markup = ReplyKeyboardRemove())
    update.message.reply_text("距離開SEM仲有"+str(days)+"日 "+str(hours)+"小時 "+str(minutes) +"分 " + str(seconds) + "秒")

def end_day(update, context):
    x = datetime.datetime.now()
    delta = datetime.datetime(2020, 12, 17,12,45) - datetime.datetime.now()
    count = (delta.total_seconds())
    days = int(count//86400)
    hours = int((count-days*86400)//3600)
    minutes = int((count-days*86400-hours*3600)//60)
    seconds = int(count-days*86400-hours*3600-minutes*60)
    #update.message.reply_text("距離完SEM仲有"+str(days)+"日 "+str(hours)+"小時 "+str(minutes) +"分 " + str(seconds) + "秒")
    update.message.reply_text("完左SEM啦仲倒數 \n用 /openday 睇下幾時開SEM",reply_markup = ReplyKeyboardRemove())

def gpa_day(update, context):
    x = datetime.datetime.now()
    delta = datetime.datetime(2021, 1, 19) - datetime.datetime.now()
    count = (delta.total_seconds())
    days = int(count//86400)
    hours = int((count-days*86400)//3600)
    minutes = int((count-days*86400-hours*3600)//60)
    seconds = int(count-days*86400-hours*3600-minutes*60)
    update.message.reply_text("距離出GPA仲有"+str(days)+"日 "+str(hours)+"小時 "+str(minutes) +"分 " + str(seconds) + "秒")

def source(update, context):
    keyboard = [
                [InlineKeyboardButton("Calculus Final Reminder", callback_data='Calculus Final Reminder')],
                 [InlineKeyboardButton("Calculus and Linear Final Review", callback_data='Calculus and Linear Final Review')],
                [InlineKeyboardButton("Calculus review", callback_data='Calculus review')],
                 [InlineKeyboardButton("Calculus_Ch1_exercise", callback_data='Calculus_Ch1_exercise')],
                  [InlineKeyboardButton("Maths Diagnostic Test", callback_data='Maths Diagnostic Test')],
                 [InlineKeyboardButton("Module 1 and 2 exercise", callback_data='Module 1 and 2 exercise')],
                  [InlineKeyboardButton("Applied Computing", callback_data='Applied Computing'),
                 InlineKeyboardButton("Programming Final Reminder", callback_data='Programming Final Reminder')],
                  [InlineKeyboardButton("Stat", callback_data='Stat'),
                 InlineKeyboardButton("CCT", callback_data='CCT')],[InlineKeyboardButton("Linear Final Reminder",callback_data='Linear Final Reminder')]
                ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)

def help_command(update, context):
    x = update.message.from_user.id
    update.message.reply_text(x,)

def dllm(update, context):
    update.message.reply_text("Hello")

def dllmcount(update, context):
    message = (update.message.text).lower()
    increaseTemp = 0
    if(update.message.reply_to_message.from_user.id is not None):
        target = update.message.reply_to_message.from_user.id
    count = 0
    if "dllm"  in message:
        DATABASE_URL = os.environ['DATABASE_URL']
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        dbCursor = conn.cursor()
        x = update.message.from_user.id
        sqlSelect = "select * from tg_user where user_id = {}".format(x)
        dbCursor.execute(sqlSelect)
        rows = dbCursor.fetchall()
        for row in rows:
           count = row[1]
        if (count == 0):
            sqlInsertTable  = "INSERT INTO tg_user values({},1,NOW()::TIMESTAMP(0))".format(x)
            print(sqlInsertTable)
        else:
            count = count + 1
            sqlInsertTable  = "UPDATE tg_user SET count = {},last_update=Now()::TIMESTAMP(0) WHERE user_id = {}".format(count,x)
        print(sqlInsertTable)
        dbCursor.execute(sqlInsertTable)
        if target is not None:
            sqlUpdate = "select * from tg_user where user_id = {}".format(target)
            dbCursor.execute(sqlUpdate)
            rows = dbCursor.fetchall()
            for row in rows:
                id = row[0]
                count = row[3]
            if (id is None):
                sqlInsertTable  = "INSERT INTO tg_user values({},0,NOW()::TIMESTAMP(0),1)".format(x)
            # elif(count == 0):
            #     sqlInsertTable  = "UPDATE tg_user SET count = {},last_update=Now()::TIMESTAMP(0),givediu = 0  WHERE user_id = {}".format(row[1],target)
            else:
                count = count + 1
                sqlInsertTable  = "UPDATE tg_user SET count = {},last_update=Now()::TIMESTAMP(0),givediu2 ={} WHERE user_id = {}".format(row[1],count,target)
            print(sqlInsertTable)
            dbCursor.execute(sqlInsertTable)
        conn.commit()
        dbCursor.close()
        conn.close()

def show(update,context):
    count = 0
    time = ""
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    dbCursor = conn.cursor()
    x = update.message.from_user.id
    sqlSelect = "select * from tg_user where user_id = {}".format(x)
    dbCursor.execute(sqlSelect)
    rows = dbCursor.fetchall()
    for row in rows:
        count = row[1]
        time = row[2]

    sqlSelect = "select * from tg_user where user_id = {}".format(x)
    dbCursor.execute(sqlSelect)
    rows = dbCursor.fetchall()
    for row in rows:
        target = row[3]
    if(count == 0):
        text1 ='你仲未講過DLLM WO'
    else:
        text1 = 'You spoke '+str(count)+' times dllm. \nLast time you speak is '+str(time)
        #update.message.reply_text(text = 'You spoke '+str(count)+' times dllm. \nLast time you speak is '+str(time))
    if(target == 0):
        text2 = '你仲未比人屌過WO'
        #update.message.reply_text(text = '你仲未比人屌過WO')
    else:
        text2 = 'You 比人屌左'+ str(target)+'次'
        #@update.message.reply_text(text = 'You 比人屌左'+ str(target)+'次')
    update.message.reply_text(text ="Broked no want fix ")


def listCanteen(update,context):
    chat_id=update.message.chat.id
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    dbCursor = conn.cursor()
    sqlSelect = "select * from canteen"
    dbCursor.execute(sqlSelect)
    rows = dbCursor.fetchall()
    menu_keyboard = []
    menu_keyboard2 = []
    latitude=""
    longitude=""
    name=""
    i = 0
    for row in rows:
        i=i+1
        latitude = row[1]
        longitude = row[2]
        name = row[3]
        menu_keyboard.append([str(name)])
        if(i%2==0):
            menu_keyboard2.append(menu_keyboard)

    menu_markup = ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(text = 'what canteen?',reply_markup=menu_markup)
    conn.commit()
    dbCursor.close()
    conn.close()


def showlocation(update,context):
    chat_id=update.message.chat.id
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    dbCursor = conn.cursor()
    sqlSelect = "select * from canteen where name = '{}'".format(update.message.text);
    dbCursor.execute(sqlSelect)
    rows = dbCursor.fetchall()
    latitude=""
    longitude=""
    name=""
    for row in rows:
        latitude = row[1]
        longitude = row[2]
        name = row[3]
    if(name != ""):
        print(name)
        context.bot.sendLocation(chat_id= chat_id, latitude=latitude, longitude=longitude,reply_markup = ReplyKeyboardRemove())



def addcanteen(update, context):
    chat_id=update.message.chat.id
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

    sqlInsertTable  = "INSERT INTO canteen (lat,long,name) values ({},{},'{}')".format(latitude,longitude,name);
    print(sqlInsertTable)
    dbCursor.execute(sqlInsertTable)
    conn.commit()
    dbCursor.close()
    conn.close()

def pin9(update,context):
    chat_id=update.message.chat.id
    f = open("pin.txt", "r")
    temp = f.read()
    update.message.reply_text(text='INFO'+temp)

def week(update,context):
    chat_id=update.message.chat.id
    today = datetime.today()
    week_number = today.isocalendar()[1]
    week_number = week_number-4
    update.message.reply_text(text='Now is Week '+str(week_number))

def exam(update,context):
    found = 0
    chat_id=update.message.chat.id
    text = ''
    text_old = ''
    file = open('Exam_timetable2.csv', 'r')

    if 'ccn' in id.lower():
        text_old = '走啦死老野'
    id = (context.args[0]).upper()
    for row in csv.reader(file):
        if row[1] == id and found == 1:
            text = text + '\nGroup ' + str(row[3]+' 既考試時間係 '+row[5])
        if row[1] == id and found == 0:
            text= text + str(row[2]+'\n既考試喺係*'+row[4]+'*\nGroup '+row[3]+' 既考試時間係'+row[5])
            found = 1
    if found == 0:
        context.bot.sendMessage(chat_id=chat_id,text = '冇呢一科牙 ' + text_old)
    else:
        context.bot.sendMessage(chat_id=chat_id,text =text, parse_mode= 'Markdown')

def username(update, context):
    username = context.args[0]
    chat_id=update.message.chat.id
    context.bot.sendMessage(chat_id=chat_id,text =username)

def important_date(update, context):
    chat_id=update.message.chat.id
    f = open('date.json',)
    data = json.load(f)
    print(data)
    tmptext=''
    for i in data['ImportantDate']:
        tmptext = tmptext+i['date']+'\n'+i['descrition']+'\n\n'
    context.bot.sendMessage(chat_id=chat_id,text =tmptext)

    
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

def checkTemp(update, context):
    #context.bot.sendMessage(chat_id=update.message.chat.id, text=str("TEST1"))
    response = requests.get("https://rss.weather.gov.hk/rss/CurrentWeather.xml")
    #context.bot.sendMessage(chat_id=update.message.chat.id,text = str("TEST2"))
    tree = ElementTree.fromstring(response.content)
    #context.bot.sendMessage(chat_id=update.message.chat.id,text = str("TEST3"))
    textTem = tree[0][7][6].text
    arraytemp = textTem.split('\n')
    for x in arraytemp:
        if(x.find("Air temperature")>=0) :
            realTemp = x.split()
            for y in realTemp:
                if(is_number(y)):
                    update.message.reply_text('今日天氣溫度係' +y+'度')


def payment(update, context):
    chat_id=update.message.chat.id
    title = "Donate"
    description = "Donate"
    payload = "Donate1228"
    provider_token = "350862534:LIVE:YjYxZjNhMjNkNmY3"
    start_parameter = "TEMP"
    currency = "HKD"
    prices = [LabeledPrice("HKCC OCAMP 費用", 1000)]
    #prices=['{"label": "donate", "amount": 300000},{"label": "donate2", "amount": 400000}']
    context.bot.sendInvoice(chat_id=chat_id,
    title=title,
    description="donate",
    payload=payload,
    provider_token=provider_token,
    start_parameter=start_parameter,
    currency=currency,
    prices=prices)


def main():
    global update_id
    TOKEN = os.environ['TOKEN']
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    #In source.py
    dp.add_handler(CommandHandler("Source", source,filters=~Filters.group))
    dp.add_handler(CommandHandler("start", start,filters=~Filters.group))
    dp.add_handler(CommandHandler("openbot", open_bot,filters=Filters.group))
    dp.add_handler(CommandHandler("openday",open_day))
    dp.add_handler(CommandHandler("endday",end_day))
    dp.add_handler(CommandHandler("gpaday",gpa_day))
    dp.add_handler(CommandHandler("date",important_date))
    dp.add_handler(CommandHandler("checkTemp",checkTemp))
    #updater.dispatcher.add_handler(CallbackQueryHandler(button))
    dp.add_handler(CommandHandler("Source", source,filters=~Filters.group))
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, newmember))
    # dp.add_handler(CommandHandler("lecturer",lecturer,filters=~Filters.group))
    #updater.dispatcher.add_handler(CallbackQueryHandler(rating))

    ############
    dp.add_handler(CommandHandler("help",help_command))
    dp.add_handler(CommandHandler("addcanteen",addcanteen,pass_args = True))
    dp.add_handler(CommandHandler("username",username,pass_args = True))


    dp.add_handler(CommandHandler("donate",payment))
    dp.add_handler(CommandHandler("canteen",listCanteen,filters=~Filters.group))
    dp.add_handler(CommandHandler("pin9",pin9,filters=Filters.group))
    dp.add_handler(CommandHandler("week",week,filters=Filters.group))

    dp.add_handler(CommandHandler("exam",exam,pass_args = True))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.group, showlocation))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    dp.add_handler(MessageHandler(Filters.text & Filters.group, dllm))

    #dp.add_handler(CommandHandler("donateToMe",donateToMe,pass_args = True))


    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://serene-depths-59599.herokuapp.com/' + TOKEN)

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
showdllmtimes - count on dllm
pin9 - show pin message
exam - exam {code} show exam date time
week - new is week ?
'''
