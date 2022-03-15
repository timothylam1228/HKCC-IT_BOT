import psycopg2
from telegram import ReplyKeyboardMarkup

def listCanteen(update, context):
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    dbCursor = conn.cursor()
    sqlSelect = "select * from canteen"
    dbCursor.execute(sqlSelect)
    rows = dbCursor.fetchall()
    menu_keyboard = []
    menu_keyboard2 = []

    name = ""
    i = 0
    for row in rows:
        i = i+1
        latitude = row[1]
        longitude = row[2]
        name = row[3]
        menu_keyboard.append([str(name)])
        if(i % 2 == 0):
            menu_keyboard2.append(menu_keyboard)

    menu_markup = ReplyKeyboardMarkup(
        menu_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(text='what canteen?', reply_markup=menu_markup)
    conn.commit()
    dbCursor.close()
    conn.close()
