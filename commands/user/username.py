def username(update, context):
    username = context.args[0]
    chat_id = update.message.chat.id

    context.bot.sendMessage(chat_id=chat_id, text=username)
