import json


def important_date(update, context):
    chat_id = update.message.chat.id
    f = open('public/date.json',)
    data = json.load(f)
    print(data)
    tmptext = ''
    for i in data['ImportantDate']:
        tmptext = tmptext+i['date']+'\n'+i['descrition']+'\n\n'
    context.bot.sendMessage(chat_id=chat_id, text=tmptext)
