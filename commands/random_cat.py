import requests


def random_cat(update, context):
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    data = response.json()
    context.bot.send_photo(
        chat_id=update.message.chat.id, photo=data[0]['url'])
