import os
import psycopg2

def message_count(update, context):
    user = update.message.from_user
    user_id = user['id']
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    dbCursor = conn.cursor()

    ### Check user exist ###
    sqlSelect = "select * from tg_user where user_id = {}".format(user_id)
    dbCursor.execute(sqlSelect)
    user = dbCursor.fetchone()
    #print('user',user)
    if not user:
        #print('empty user')
        sqlInsertTable = "INSERT INTO tg_user values({},0,NOW()::TIMESTAMP(0),1)".format(user_id)
    else:
        sqlSelect = "select marks from tg_user where user_id = {}".format(user_id)
        dbCursor.execute(sqlSelect)
        mark = dbCursor.fetchone()
        if mark is not None:
            mark = mark[0]
        #print('mark',mark)
        mark = mark + 1
        sqlInsertTable = "UPDATE tg_user SET marks = {} , last_update=Now()::TIMESTAMP(0) WHERE user_id = {}".format(mark, user_id)
    dbCursor.execute(sqlInsertTable)
    conn.commit()
    dbCursor.close()
    conn.close()

'''


'''