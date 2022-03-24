def pin9(update, context):
    chat_id = update.message.chat.id
    f = open("public/pin.txt",encoding="utf8")
    temp = f.read()
    # update.message.reply_text(text='INFO'+temp)
    context.bot.sendMessage(chat_id=chat_id, text=temp, parse_mode='HTML')
