import os
import psycopg2


def show_dllm(update, context):
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
        text1 = '你仲未講過DLLM WO'
    else:
        text1 = 'You spoke ' + \
            str(count)+' times dllm. \nLast time you speak is '+str(time)
        #update.message.reply_text(text = 'You spoke '+str(count)+' times dllm. \nLast time you speak is '+str(time))
    if(target == 0):
        text2 = '你仲未比人屌過WO'
        #update.message.reply_text(text = '你仲未比人屌過WO')
    else:
        text2 = 'You 比人屌左' + str(target)+'次'
        # @update.message.reply_text(text = 'You 比人屌左'+ str(target)+'次')
    update.message.reply_text(text="Broked no want fix ")
