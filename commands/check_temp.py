import requests
from xml.etree import ElementTree


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def checkTemp(update, context):
    #context.bot.sendMessage(chat_id=update.message.chat.id, text=str("TEST1"))
    response = requests.get(
        "https://rss.weather.gov.hk/rss/CurrentWeather.xml")
    #context.bot.sendMessage(chat_id=update.message.chat.id,text = str("TEST2"))
    tree = ElementTree.fromstring(response.content)
    #context.bot.sendMessage(chat_id=update.message.chat.id,text = str("TEST3"))
    textTem = tree[0][7][6].text
    arraytemp = textTem.split('\n')
    for x in arraytemp:
        if(x.find("Air temperature") >= 0):
            realTemp = x.split()
            for y in realTemp:
                if(is_number(y)):
                    update.message.reply_text('今日天氣溫度係' + y+'度')
