
"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import random
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler
from telegram import InlineQuery , ReplyKeyboardMarkup, ReplyKeyboardRemove, MessageEntity, ForceReply, InlineKeyboardButton,InlineKeyboardMarkup
from telegram.utils import helpers
import datetime


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
    
logger = logging.getLogger(__name__)
REQUEST, PHOTO, LOCATION, BIO = range(4)
CHECK_THIS_OUT = 'check-this-out'
USING_ENTITIES = 'using-entities-here'
SO_COOL = 'so-cool'
TEMP = 0
# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('/source for Geting the source')


def help_command(update, context):
    return 
    
   
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



def question(update, context):
    if(update.message.text)== 'Question':
        update.message.reply_text('No Question are allowed',reply_markup=ReplyKeyboardRemove())
    elif(update.message.text)== 'Source':
        update.message.reply_text('No Source ar dllm',reply_markup=ReplyKeyboardRemove())
    # if ((update.message.text).lower()  == 'Source'):
    return ConversationHandler.END


def cancel(update, context):
    update.message.reply_text('Bye!',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

def echo(update, context):
    """Echo the user message."""
    x = update.message.from_user.id
    print(x)
    if(x == 197183803):
        update.message.reply_text('DLLM')
    # if((update.message.text).lower() == 'dllm'):
        
        #context.bot.delete_message(update.message.message_id,update.message)
        # context.bot.deleteMessage(chat_id=update.message.chat.id, message_id=update.message.message_id)
        # global TEMP
        # TEMP = TEMP + 1
        # if(TEMP%5==0):
        #     context.bot.sendMessage(chat_id=update.message.chat.id,text =  str(update.message.from_user.first_name) + ' Dont say dllm plz, you speaked '+str(TEMP)+' times ' )

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
    # file="source/CCT.pdf"
    # # send the pdf doc
    # bot.sendDocument(chat_id=update.message.chat.id, document=open(file, 'rb'))
      
    
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
        InlineKeyboardButton(text='Private Chat with bot here!', url=url)
    )
    #context.bot.sendMessage(chat_id=update.message.chat.id,text ="        Hello",reply_markup=keyboard)
    update.message.reply_text("Hello", reply_markup=keyboard)

def open_day(update, context):
    x = datetime.datetime.now()
    delta = datetime.datetime(2020, 9, 7) - datetime.datetime.now()
    count = (delta.total_seconds())
    days = int(count//86400)
    hours = int((count-days*86400)//3600)
    minutes = int((count-days*86400-hours*3600)//60)
    seconds = int(count-days*86400-hours*3600-minutes*60)
    update.message.reply_text("距離開學仲有"+str(days)+"日 "+str(hours)+"小時 "+str(minutes) +"分 " + str(seconds) + "秒")

def main():
    global update_id
    
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    # Welcome 1357264168:AAHSA6t5WsWkZ3pl4B8-z8CWcaneZUJpw-Q
    #
    updater = Updater("1274514043:AAGusVpMUbN8vn8Jy-qWMmoc3GJXUszi13k", use_context=True)
 
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start,filters=~Filters.group))
    dp.add_handler(CommandHandler("help",help_command))
    dp.add_handler(CommandHandler("openbot", open_bot,filters=Filters.group))
    dp.add_handler(CommandHandler("openday",open_day))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler(Filters.text & ~Filters.command , echo))
    #dp.add_handler(MessageHandler(Filters.sticker, echo))
    dp.add_handler(CommandHandler("Source", source,filters=~Filters.group))
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, newmember))
    # Start the Bot
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