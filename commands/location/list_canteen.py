import psycopg2
from telegram import ReplyKeyboardMarkup
import os

import utils.database 
def listCanteen(update, context):
    dbCursor = connect()
    sqlSelect = "select * from tg_user"
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
