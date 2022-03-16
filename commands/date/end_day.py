from datetime import datetime
from telegram import ReplyKeyboardRemove
import json


def end_day(update, context):
    f = open('commands/date/important_date.json')
    data = json.load(f)
    x = datetime.now()
    delta = datetime.fromisoformat(data['end_date']) - datetime.now()
    count = (delta.total_seconds())
    days = int(count//86400)
    hours = int((count-days*86400)//3600)
    minutes = int((count-days*86400-hours*3600)//60)
    seconds = int(count-days*86400-hours*3600-minutes*60)
    if days >= 0:
        update.message.reply_text(
            "距離完SEM仲有"+str(days)+"日 "+str(hours)+"小時 "+str(minutes) + "分 " + str(seconds) + "秒")
    else:
        update.message.reply_text(
            "完左SEM啦仲倒數 \n用 /openday 睇下幾時開SEM", reply_markup=ReplyKeyboardRemove())
