# coding=UTF-8


from telegram.ext import PreCheckoutQueryHandler,Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton
import os
from dotenv import load_dotenv
from commands.init import *
from telegram.bot import Bot, BotCommand
'''
openbot - open the bot
openday - remaining time b4 hell
endday - remaining time to leave hell
gpaday - most excited day
pin9 - show pin message
exam - exam {code} show exam date time
week - now is week ?
show_marks - show your marks
check_temp - check today temperature
samgor - today eat wt ho
bam - ban message user when 5 users use this command 
'''

load_dotenv()
commands = [
('openbot', 'Open the bot'),
('pin9', 'Pin message'),
('bam', 'Ban user'),
('samgor', 'Eat what'),
('checkTemp', 'Check temperature'),
('wantCat', 'Random cat'),
('show_marks', 'Show your marks'),
]
def main():
    global update_id
    PORT = int(os.environ.get('PORT', 8443))

    if os.environ['APP_ENV'] == 'LOCAL':
        TOKEN = os.environ.get('LOCAL_TOKEN')
        print(TOKEN)
    else:
        TOKEN = os.environ.get('TOKEN')
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    # bot = Bot(TOKEN)
    # bot.set_my_commands(commands)

    #Date
    dp.add_handler(CommandHandler("openday", open_day))
    dp.add_handler(CommandHandler("endday", end_day))
    dp.add_handler(CommandHandler("gpaday", gpa_day))
    dp.add_handler(CommandHandler("date", important_date))
    dp.add_handler(CommandHandler("week", week, filters=Filters.chat_type.groups))
    dp.add_handler(CommandHandler("exam", exam, pass_args=True))

    #Function
    dp.add_handler(CommandHandler("checkTemp", checkTemp))
    dp.add_handler(CommandHandler("wantCat", random_cat))
    dp.add_handler(CommandHandler("samgor", samgor, pass_args=True))


    #Source
    dp.add_handler(CommandHandler("source", source, filters=~Filters.chat_type.groups))
    dp.add_handler(CommandHandler("start", start, filters=~Filters.chat_type.groups))
    dp.add_handler(CommandHandler("openbot", open_bot, filters=Filters.chat_type.groups))


    #Bot
    #dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, newmember))
    dp.add_handler(CommandHandler('bam',ban, filters=Filters.chat_type.groups))
    dp.add_handler(CommandHandler('unbam',unban, filters=Filters.chat_type.groups))
    dp.add_handler(CommandHandler('bam_show',ban_show, filters=Filters.chat_type.groups))

    dp.add_handler(CommandHandler("pin9", pin9, filters=Filters.chat_type.groups))
    dp.add_handler(CommandHandler("username", username, pass_args=True))
    dp.add_handler(CommandHandler("dllmcount", dllmcount, filters=~Filters.chat_type.groups))
    dp.add_handler(CommandHandler("show_dllm",show_dllm))

    dp.add_handler(CommandHandler("show_marks",show_marks))
    dp.add_handler(CommandHandler("show_message_id",show_marks))

    dp.add_handler(MessageHandler(Filters.text, message_count))

    #Useless
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    dp.add_handler(CommandHandler("ocampfee", payment, pass_args=True))
    dp.add_handler(MessageHandler(
        Filters.successful_payment, successful_payment_callback))
    dp.add_handler(PreCheckoutQueryHandler(precheckout_callback))
    # dp.add_handler(CommandHandler(
    #     "canteen", listCanteen, filters=~Filters.chat_type.groups))


    webhook_url = 'https://hkcc-it-bot.herokuapp.com/' + TOKEN

    if os.environ['APP_ENV'] == 'LOCAL':
        print('======================Starting with local port'+  str(PORT) + '====================== ')

        # updater.start_webhook(listen="0.0.0.0",
        #                       port=8443,
        #                       url_path=TOKEN,
        #                       webhook_url=webhook_url)
    else:
        print('======================Starting with port '+ str(PORT) + '====================== ')
        updater.start_webhook(listen="0.0.0.0",
                              port=PORT,
                              url_path=TOKEN,
                              webhook_url=webhook_url)


    
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
  

