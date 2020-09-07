#coding=UTF-8

import logging
import random
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler,StringCommandHandler
from telegram import InlineQuery , ReplyKeyboardMarkup, ReplyKeyboardRemove, MessageEntity, ForceReply, InlineKeyboardButton,InlineKeyboardMarkup
from telegram.utils import helpers
import datetime
import os
import psycopg2

PORT = int(os.environ.get('PORT', 5000))
SO_COOL = 'hkcc-it'

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
    
logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('/source for Geting the source')

def newmember(update, context):
    """Send a message when the command /help is issued."""
    bot = context.bot
    url = helpers.create_deep_linked_url(bot.get_me().username, SO_COOL)
    text = "歡迎來到IT谷" 
    keyboard = InlineKeyboardMarkup.from_button(
        InlineKeyboardButton(text='Continue here!', url=url)
    )
    update.message.reply_text(text, reply_markup=keyboard)

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
    delta = datetime.datetime(2020, 9, 7) - datetime.datetime.now()
    count = (delta.total_seconds())
    if(count<=0):
        update.message.reply_text("開左學啦仲倒數 \n用 /endday 睇下幾時完SEM")
    else:
        days = int(count//86400)
        hours = int((count-days*86400)//3600)
        minutes = int((count-days*86400-hours*3600)//60)
        seconds = int(count-days*86400-hours*3600-minutes*60)
        update.message.reply_text("距離開學仲有"+str(days)+"日 "+str(hours)+"小時 "+str(minutes) +"分 " + str(seconds) + "秒")

def end_day(update, context):
    x = datetime.datetime.now()
    delta = datetime.datetime(2021, 1, 3) - datetime.datetime.now()
    count = (delta.total_seconds())
    days = int(count//86400)
    hours = int((count-days*86400)//3600)
    minutes = int((count-days*86400-hours*3600)//60)
    seconds = int(count-days*86400-hours*3600-minutes*60)
    update.message.reply_text("距離完SEM仲有"+str(days)+"日 "+str(hours)+"小時 "+str(minutes) +"分 " + str(seconds) + "秒")

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
                 InlineKeyboardButton("CCT", callback_data='CCT')],
                ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)

def help_command(update, context):
    x = update.message.from_user.id
    update.message.reply_text(x)

def dllmcount(update, context):
    message = (update.message.text).lower()
    increaseTemp = 0
    count = 0
    if "dllm"  in message:
        DATABASE_URL = os.environ['DATABASE_URL']
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        dbCursor = conn.cursor();
        x = update.message.from_user.id
        sqlSelect = "select * from tg_user where user_id = {}".format(x);
        dbCursor.execute(sqlSelect)
        rows = dbCursor.fetchall()
        for row in rows:
           count = row[1]
        if (count == 0):
            sqlInsertTable  = "INSERT INTO tg_user values({},1,NOW()::TIMESTAMP(0))".format(x);
            print(sqlInsertTable)
        else:
            count = count + 1
            sqlInsertTable  = "UPDATE tg_user SET count = {},last_update=Now()::TIMESTAMP(0)  WHERE user_id = {}".format(count,x);
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
    dbCursor = conn.cursor();
    x = update.message.from_user.id
    sqlSelect = "select * from tg_user where user_id = {}".format(x);
    dbCursor.execute(sqlSelect)
    rows = dbCursor.fetchall()
    for row in rows:
        count = row[1]
        time = row[2]
    if(count == 0):
        update.message.reply_text(text = '你仲未講過DLLM WO ')
    else:
        update.message.reply_text(text = 'You spoke '+str(count)+' times dllm. \nLast time you speak is '+str(time))

def listCanteen(update,context):
    chat_id=update.message.chat.id
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    dbCursor = conn.cursor();
    sqlSelect = "select * from canteen";
    dbCursor.execute(sqlSelect)
    rows = dbCursor.fetchall()
    menu_keyboard = []
    latitude=""
    longitude=""
    name=""
    for row in rows:
        latitude = row[1]
        longitude = row[2]
        name = row[3]
        menu_keyboard.append([str(name)])
    menu_markup = ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(text = 'what canteen?',reply_markup=menu_markup)
    conn.commit()
    dbCursor.close()
    conn.close()
    return ConversationHandler.END

def showlocation(update,context):
    chat_id=update.message.chat.id
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    dbCursor = conn.cursor();
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
    dbCursor = conn.cursor();
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
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    dp.add_handler(CommandHandler("Source", source,filters=~Filters.group))
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, newmember))
    ############
    dp.add_handler(CommandHandler("help",help_command))
    dp.add_handler(CommandHandler("addcanteen",addcanteen,pass_args = True))
    dp.add_handler(CommandHandler("showdllmtimes",show))
    dp.add_handler(CommandHandler("canteen",listCanteen))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.group & ~Filters.group, showlocation))

    updater.dispatcher.add_handler(CallbackQueryHandler(button))
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
'''