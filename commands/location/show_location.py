# def showlocation(update, context):
#     chat_id = update.message.chat.id
#     DATABASE_URL = os.environ['DATABASE_URL']
#     conn = psycopg2.connect(DATABASE_URL, sslmode='require')
#     dbCursor = conn.cursor()
#     sqlSelect = "select * from canteen where name = '{}'".format(
#         update.message.text)
#     dbCursor.execute(sqlSelect)
#     rows = dbCursor.fetchall()
#     latitude = ""
#     longitude = ""
#     name = ""
#     for row in rows:
#         latitude = row[1]
#         longitude = row[2]
#         name = row[3]
#     if(name != ""):
#         print(name)
#         context.bot.sendLocation(chat_id=chat_id, latitude=latitude,
#                                  longitude=longitude, reply_markup=ReplyKeyboardRemove())


