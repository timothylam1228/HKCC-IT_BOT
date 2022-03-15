from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.utils import helpers
SO_COOL = 'hkcc-it'


def newmember(update, context):
    """Send a message when the command /help is issued."""
    query = update.callback_query
    bot = context.bot
    url = helpers.create_deep_linked_url(bot.get_me().username, SO_COOL)
    text = "歡迎來到IT谷"
    keyboard = InlineKeyboardMarkup.from_button(
        InlineKeyboardButton(text='Continue here!', url=url)
    )
    ogg_url = 'https://github.com/timothylam1228/CodeDeployGitHubDemo/raw/master/source/plato.ogg'
    for member in update.message.new_chat_members:
        update.message.reply_text(text, reply_markup=keyboard)
        context.bot.send_voice(chat_id=update.message.chat.id, voice=ogg_url)
        new_members = update.message.new_chat_members
        firstname = member.first_name
        lastname = member.last_name
        if("+852" in firstname):
            bot.kick_chat_member(chat_id=update.message.chat.id,
                                 user_id=update.message.from_user.id)
            return
        elif("+852" in lastname):
            bot.kick_chat_member(chat_id=update.message.chat.id,
                                 user_id=update.message.from_user.id)
            return
