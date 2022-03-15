import datetime
from telegram import ReplyKeyboardRemove


def open_day(update, context):
    x = datetime.datetime.now()
    delta = datetime.datetime(2021, 9, 6) - datetime.datetime.now()
    count = (delta.total_seconds())
    days = int(count//86400)
    hours = int((count-days*86400)//3600)
    minutes = int((count-days*86400-hours*3600)//60)
    seconds = int(count-days*86400-hours*3600-minutes*60)
    if days >= 0:
        update.message.reply_text(
            "距離開SEM仲有"+str(days)+"日 "+str(hours)+"小時 "+str(minutes) + "分 " + str(seconds) + "秒")
    else:
        update.message.reply_text(
            "開左學啦仲倒數 \n用 /endday 睇下幾時完SEM", reply_markup=ReplyKeyboardRemove())