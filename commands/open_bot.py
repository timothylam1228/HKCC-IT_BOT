from telegram.utils import helpers
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
SO_COOL = 'hkcc-it'


def open_bot(update, context):
    x = update.message.from_user.id
    print(x)
    bot = context.bot
    url = helpers.create_deep_linked_url(bot.get_me().username, SO_COOL)
    keyboard = InlineKeyboardMarkup.from_button(
        InlineKeyboardButton(text='Get Resource here!', url=url)
    )
    update.message.reply_text("Hello", reply_markup=keyboard)
