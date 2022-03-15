import json
import random


def samgor(update, context):
    chat_id = update.message.chat.id
    try:
        number1 = int(context.args[0].strip())
        if(number1 > 26 or number1 < 0):
            update.message.reply_text('請輸入範圍 1-25')
            return
        f = open('samgor.json',)
        data = json.load(f)
        randomIngredient = random.sample(range(25), number1)
        randomSoupBase = random.sample(range(6), 1)
        randomSpiciness = random.sample(range(10), 1)
        randomAppetizers = random.sample(range(9), 1)
        randomSnacksForOne = random.sample(range(6), 1)
        randomDrink = random.sample(range(15), 1)
        eattext = ''
        eattext = '今日三哥食咩好\n\n'
        if(number1 != 0):
            eattext = eattext + str(number1) + ' 餸 : \n'
            for i in range(number1):
                eattext = eattext + \
                    data['Ingredient'][randomIngredient[i]]['name']+' '
            eattext = eattext + '\n\n'
        eattext = eattext + '湯底 : \n'
        eattext = eattext + \
            data['SoupBase'][randomSoupBase[0]]['name'] + '\n\n'
        eattext = eattext + '辣度 : \n'
        if randomSoupBase[0] == 4 or randomSoupBase[0] == 5:
            eattext = eattext + '無辣比你揀呀 88 \n\n'
        else:
            eattext = eattext + \
                data['Spiciness'][randomSpiciness[0]]['name'] + '\n\n'
        eattext = eattext + '三哥小食 : \n'
        eattext = eattext + \
            data['Appetizers'][randomAppetizers[0]]['name'] + '\n\n'
        eattext = eattext + '一人小食 : \n'
        eattext = eattext + \
            data['SnacksForOne'][randomSnacksForOne[0]]['name'] + '\n\n'
        eattext = eattext + '飲品 : \n'
        eattext = eattext + data['Drink'][randomDrink[0]]['name'] + '\n'
        context.bot.sendMessage(chat_id=chat_id, text=eattext)
    except (IndexError, ValueError):
        update.message.reply_text('請輸入範圍 1-25')
