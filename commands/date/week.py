import datetime


def week(update, context):
    chat_id = update.message.chat.id
    today = datetime.datetime.today()
    week_number = today.isocalendar()[1]
    week_number = week_number-4
    update.message.reply_text(text='Now is Week '+str(week_number))
