from telebot import types


def Start_Handler(message, bot):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='نظردهی', callback_data='commenting'))
    bot.send_message(
        message.chat.id,
        f'کاربرگرامی {message.from_user.first_name} به ربات ثبت نظر خوش آمدید برای ثبت نظر از دکمه های پایین استفاده کنید.',
        reply_markup=keyboard
    )
