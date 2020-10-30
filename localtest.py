#coding=UTF-8

import logging
import random
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
from telegram import InlineQuery , ReplyKeyboardMarkup, ReplyKeyboardRemove, MessageEntity, ForceReply, InlineKeyboardButton,InlineKeyboardMarkup
from telegram.utils import helpers
import datetime
import os
import psycopg2
PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
    
logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.


def help_command(update, context):
    x = update.message.from_user.id
    update.message.reply_text(x)

def dllmcount(update, context):
    text = update.message.text
    if(text.lower() =='dllm'):
        DATABASE_URL = os.environ['DATABASE_URL']
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        dbCursor = conn.cursor();
        x = update.message.from_user.id
        sqlSelect = "select count from tg_user where user id = {}".format(x);
        dbCursor.execute(sqlSelect)
        count = dbCursor.fetchall()
        currentTime = datetime.datetime.now()
        count = count + 1
        if (count == ''):
            sqlInsertTable  = "INSERT INTO tg_user values({},1,{})".format(x,currentTime);
        else:
            sqlInsertTable  = "UPDATE tg_user SET count = {} WHERE user_id = {}".format(count,x);

        dbCursor.execute(sqlInsertTable)

    
def main():
    global update_id
  
    # Welcome 1357264168:AAHSA6t5WsWkZ3pl4B8-z8CWcaneZUJpw-Q


    TOKEN = '1274514043:AAGz_y2lKFk3ThHB5W4Mc6K05YK3B-IGXio'
    updater = Updater("1274514043:AAGz_y2lKFk3ThHB5W4Mc6K05YK3B-IGXio", use_context=True)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("help",help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command , dllmcount))
    # Start the Bot
    # updater.start_webhook(listen="0.0.0.0",
    #                       port=int(PORT),
    #                       url_path=TOKEN)
    # updater.bot.setWebhook('https://serene-depths-59599.herokuapp.com/' + TOKEN)
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()



'''
openbot - open the bot
openday - remaining time b4 hell
'''