import os
import psycopg2


def show_marks(update, context):
    print('show_marks')
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    dbCursor = conn.cursor()
    user = update.message.from_user
    user_id = user['id']
    sqlSelect = "select marks from tg_user where user_id = {}".format(user_id)
    dbCursor.execute(sqlSelect)
    mark = dbCursor.fetchone()
    mark = mark[0]
    print(mark)
    if(mark == 0):
        text1 = '你仲未有分'
    else:
        text1 = '你有' + str(mark)+'分'
        #update.message.reply_text(text = 'You spoke '+str(count)+' times dllm. \nLast time you speak is '+str(time))

    update.message.reply_text(text=text1)
