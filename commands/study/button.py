from telegram import InlineKeyboardButton
def button(update, context):
    print('update.callback_query',update.callback_query.answer())
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    query.edit_message_text(text="Selected option: {}".format(query.data))
    path = "https://raw.githubusercontent.com/timothylam1228/HKCC-IT_BOT/master/public/source/"
    file = str(query.data)
    pdf = ".pdf"
    jpg = ".jpg"
    context.bot.sendDocument(
        chat_id=query.message.chat.id, document=path+file+pdf)
    if(file == "Maths Diagnostic Test"):
        context.bot.sendPhoto(chat_id=query.message.chat.id,
                              photo='https://raw.githubusercontent.com/timothylam1228/HKCC-IT_BOT/master/public/source/maths_diagonositc_test_changed.jpg')
        context.bot.sendMessage(
            chat_id=query.message.chat.id, text=" Q7.6 has update Please be careful")

