from datetime import datetime
import json


def gpa_day(update, context):
    x = datetime.now()
    f = open('../important_date.json',)
    data = json.load(f)
    delta = datetime.fromisoformat(data['gpa_date']) - datetime.now()
    count = (delta.total_seconds())
    days = int(count//86400)
    hours = int((count-days*86400)//3600)
    minutes = int((count-days*86400-hours*3600)//60)
    seconds = int(count-days*86400-hours*3600-minutes*60)
    update.message.reply_text(
        "距離出GPA仲有"+str(days)+"日 "+str(hours)+"小時 "+str(minutes) + "分 " + str(seconds) + "秒")
