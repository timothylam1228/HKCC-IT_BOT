

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import os



def source(update, context):

    list_keyboard = []
    directory = os.fsencode('public/source')
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        filename = os.path.splitext(filename)[0]
        data = [InlineKeyboardButton(filename,callback_data=filename)]
        list_keyboard.append(data)
 
    keyboard = [
        [InlineKeyboardButton("Calculus Final Reminder",
                              callback_data='Calculus Final Reminder')],
        [InlineKeyboardButton("Calculus and Linear Final Review",
                              callback_data='Calculus and Linear Final Review')],
        [InlineKeyboardButton(
            "Calculus review", callback_data='Calculus review')],
        [InlineKeyboardButton("Calculus_Ch1_exercise",
                              callback_data='Calculus_Ch1_exercise')],
        [InlineKeyboardButton("Maths Diagnostic Test",
                              callback_data='Maths Diagnostic Test')],
        [InlineKeyboardButton("Module 1 and 2 exercise",
                              callback_data='Module 1 and 2 exercise')],
        [InlineKeyboardButton("Applied Computing", callback_data='Applied Computing'),
         InlineKeyboardButton("Programming Final Reminder", callback_data='Programming Final Reminder')],
        [InlineKeyboardButton("Stat", callback_data='Stat'),
         InlineKeyboardButton("CCT", callback_data='CCT')], [InlineKeyboardButton("Linear Final Reminder", callback_data='Linear Final Reminder')]
    ]

    reply_markup = InlineKeyboardMarkup(list_keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)

