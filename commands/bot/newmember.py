from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.utils import helpers
SO_COOL = 'hkcc-it'
import psycopg2
import os
import time
def newmember(update, context):
    """Send a message when the command /help is issued."""
    query = update.callback_query
    bot = context.bot
    user_id = update.message.from_user.id
    url = helpers.create_deep_linked_url(bot.get_me().username, SO_COOL)
    text = "歡迎來到IT谷"
    keyboard = InlineKeyboardMarkup.from_button(
        InlineKeyboardButton(text='Continue here!', url=url)
    )
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    dbCursor = conn.cursor()

    ogg_url = 'https://github.com/timothylam1228/CodeDeployGitHubDemo/raw/master/source/plato.ogg'
    for member in update.message.new_chat_members:
        message_delete = update.message.reply_text(text, reply_markup=keyboard)
        message_delete2 = context.bot.send_voice(chat_id=update.message.chat.id, voice=ogg_url)
        firstname = member.first_name
        lastname = member.last_name

        #upload user to db
        sqlInsert = "INSERT INTO tg_user values({},0,NOW()::TIMESTAMP(0),1)".format(member.id)

        # sqlInsert = "INSERT INTO tg_user (user_id, last_update) VALUES (%d, Now()::TIMESTAMP(0))" % (user_id)
        dbCursor.execute(sqlInsert)

        if("+852" in firstname):
            bot.kick_chat_member(chat_id=update.message.chat.id,
                                 user_id=update.message.from_user.id)
            
        elif("+852" in lastname):
            bot.kick_chat_member(chat_id=update.message.chat.id,
                                 user_id=update.message.from_user.id)
        conn.commit()
        dbCursor.close()
        conn.close()
        break
    #remove bot message
    time.time.sleep(5)
    context.bot.delete_message(chat_id=update.message.chat.id, message_id=message_delete.message_id)
    context.bot.delete_message(chat_id=update.message.chat.id, message_id=message_delete2.message_id)