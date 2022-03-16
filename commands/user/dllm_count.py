import os
import psycopg2

def dllmcount(update, context):
   
    message = (update.message.text).lower()
    increaseTemp = 0
    if(update.message.reply_to_message.from_user.id is not None):
        target = update.message.reply_to_message.from_user.id
    count = 0
    if "dllm" in message:
        DATABASE_URL = os.environ['DATABASE_URL']
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        dbCursor = conn.cursor()
        x = update.message.from_user.id
        sqlSelect = "select * from tg_user where user_id = {}".format(x)
        dbCursor.execute(sqlSelect)
        rows = dbCursor.fetchall()
        for row in rows:
            count = row[3]
        if (count == 0):
            sqlInsertTable = "INSERT INTO tg_user values({},1,NOW()::TIMESTAMP(0))".format(
                x)
            print(sqlInsertTable)
        else:
            count = count + 1
            sqlInsertTable = "UPDATE tg_user SET count = {},last_update=Now()::TIMESTAMP(0) WHERE user_id = {}".format(count, x)
        print(sqlInsertTable)
        dbCursor.execute(sqlInsertTable)
        if target is not None:
            sqlUpdate = "select * from tg_user where user_id = {}".format(
                target)
            dbCursor.execute(sqlUpdate)
            rows = dbCursor.fetchall()
            for row in rows:
                id = row[0]
                count = row[3]
            if (id is None):
                sqlInsertTable = "INSERT INTO tg_user values({},0,NOW()::TIMESTAMP(0),1)".format(
                    x)
            # elif(count == 0):
            #     sqlInsertTable  = "UPDATE tg_user SET count = {},last_update=Now()::TIMESTAMP(0),givediu = 0  WHERE user_id = {}".format(row[1],target)
            else:
                count = count + 1
                sqlInsertTable = "UPDATE tg_user SET count = {},last_update=Now()::TIMESTAMP(0),givediu2 ={} WHERE user_id = {}".format(
                    row[1], count, target)
            print(sqlInsertTable)
            dbCursor.execute(sqlInsertTable)
        conn.commit()
        dbCursor.close()
        conn.close()
