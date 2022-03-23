
import os
import psycopg2

SO_COOL = 'hkcc-it'

def ban_show(update, context):
    """Send a message when the command /help is issued."""
    chat_id = update.message.chat.id
    message_id = update.message.reply_to_message.message_id
    from_user = update.message.from_user
    from_user_id = from_user['id']
    user =  update.message.reply_to_message.from_user
    to_user_id = user['id']
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    conn.autocommit = True
    dbCursor = conn.cursor()
    sqlSelect = "select * from tg_user where user_id = {}".format(to_user_id)
    dbCursor.execute(sqlSelect)
    user = dbCursor.fetchone()
    if user[0] is not None:
        checkDuplicateBanUser = "select ban_users from tg_user where user_id = {}".format(to_user_id)
        dbCursor.execute(checkDuplicateBanUser)
        ban_user_list = dbCursor.fetchone()
        ban_user_list = ban_user_list[0]
       
        sqlSelect_count = "select ban_count from tg_user where user_id = {}".format(to_user_id)
        dbCursor.execute(sqlSelect_count)
        ban_count = dbCursor.fetchone()

        ban_count = ban_count[0]

        text = "你比人警告左" + str(ban_count) + "次\n"
        update.message.reply_text(reply_to_message_id=message_id, text=str(text))



                # if count >= 5:

    # bot = context.bot
    # url = helpers.create_deep_linked_url(bot.get_me().username, SO_COOL)
    # text = "歡迎來到IT谷"
    # keyboard = InlineKeyboardMarkup.from_button(
    #     InlineKeyboardButton(text='Continue here!', url=url)
    # )
    # ogg_url = 'https://github.com/timothylam1228/CodeDeployGitHubDemo/raw/master/source/plato.ogg'
    # for member in update.message.new_chat_members:
    #     update.message.reply_text(text, reply_markup=keyboard)
    #     context.bot.send_voice(chat_id=update.message.chat.id, voice=ogg_url)
    #     new_members = update.message.new_chat_members
    #     firstname = member.first_name
    #     lastname = member.last_name
    #     if("+852" in firstname):
    #         bot.kick_chat_member(chat_id=update.message.chat.id,
    #                              user_id=update.message.from_user.id)
    #         return
    #     elif("+852" in lastname):
    #         bot.kick_chat_member(chat_id=update.message.chat.id,
    #                              user_id=update.message.from_user.id)
    #         return