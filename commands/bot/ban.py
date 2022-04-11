
import os
import psycopg2

SO_COOL = 'hkcc-it'

def checkUserExist(dbCursor, id):
    sqlSelect = "select * from tg_user where user_id = {}".format(id)
    dbCursor.execute(sqlSelect)
    user = dbCursor.fetchone()
    if user is None:
        sqlInsertTable = "INSERT INTO tg_user values({},0,NOW()::TIMESTAMP(0),1)".format(id)
        dbCursor.execute(sqlInsertTable)
    return True

def ban(update, context):
    """Send a message when the command /help is issued."""
    chat_id = update.message.chat.id
    message_id = update.message.reply_to_message.message_id
    from_user = update.message.from_user
    from_user_id = from_user['id']
    user = update.message.reply_to_message.from_user
    to_user_id = user['id'] #block ppl
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    conn.autocommit = True
    dbCursor = conn.cursor()
    checkUserExist(dbCursor, from_user_id)
    checkUserExist(dbCursor, to_user_id)

    if from_user_id == to_user_id:
        update.message.reply_text('?')
    else:
        checkDuplicateBanUser = "select 1 from tg_user_bam_relationship where user_id = {} AND block_user_id = {}".format(to_user_id, from_user_id)
        dbCursor.execute(checkDuplicateBanUser)
        ban_user_list = dbCursor.fetchone()
        if ban_user_list is not None:
            if ban_user_list == 1:
                update.message.reply_text('You already bamed')
        else:
            insert_sql = "INSERT INTO tg_user_bam_relationship (user_id, block_user_id) VALUES ({},{})".format(to_user_id, from_user_id)
            #sqlSelect_count = "select ban_count from tg_user where user_id = {}".format(to_user_id)
            dbCursor.execute(insert_sql)

            sqlSelect_bancount = "SELECT COUNT(*) from tg_user_bam_relationship Where user_id = {}".format(to_user_id)
            dbCursor.execute(sqlSelect_bancount)
            ban_count = dbCursor.fetchone()
            ban_count = ban_count[0]
        
            if ban_count >= 5 :
                ban_text = "你比人警告左" + str(ban_count) + "次\nBye"
                update.message.reply_text(reply_to_message_id=message_id, text=str(ban_text))
                context.bot.ban_chat_member(chat_id=chat_id,user_id=to_user_id)
            else:
                text = "你比人警告左" + str(ban_count) + "次\n5次警告會BAMMMMMMMM"
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