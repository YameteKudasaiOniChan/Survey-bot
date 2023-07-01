from comment import Comment, comment_dict
from telebot import types


def Quest1(message, bot):
    name = message.text
    chat_id = message.chat.id
    data = Comment(name)
    comment_dict[chat_id] = data
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add('عالی')
    keyboard.add('متوسط')
    keyboard.add('ضعیف')
    msg = bot.send_message(
        chat_id,
        """
مرحله اول:
کیفیت کالای خریداری شده چگونه بود؟
        """,
        reply_markup=keyboard
    )
    return msg


def Quest2(message, bot):
    chat_id = message.chat.id
    comment = comment_dict[chat_id]
    comment.quest_1 = message.text
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add('عالی')
    keyboard.add('متوسط')
    keyboard.add('ضعیف')
    msg = bot.send_message(
        chat_id,
        """
مرحله دوم:
زمان بندی ارسال محصول پگونه بود؟
        """,
        reply_markup=keyboard
    )
    return msg


def Quest3(message, bot):
    chat_id = message.chat.id
    comment = comment_dict[chat_id]
    comment.quest_2 = message.text
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add('عالی')
    keyboard.add('متوسط')
    keyboard.add('ضعیف')
    msg = bot.send_message(
        chat_id,
        """
مرحله سوم:
بسته بندی محصول چطور بود؟
        """,
        reply_markup=keyboard
    )
    return msg


def Quest4(message, bot):
    chat_id = message.chat.id
    comment = comment_dict[chat_id]
    comment.quest_3 = message.text
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add('بالا تر')
    keyboard.add('متوسط')
    keyboard.add('پایین تر')
    msg = bot.send_message(
        chat_id,
        """
مرحله چهارم:
قیمت محصول نسبط به جاهای دیگر چطور بود؟
        """,
        reply_markup=keyboard
    )
    return msg


def Quest5(message, bot):
    chat_id = message.chat.id
    comment = comment_dict[chat_id]
    comment.quest_4 = message.text
    keyboard = types.ReplyKeyboardRemove()
    msg = bot.send_message(
        chat_id,
        """
مرحله پنجم:
نظر خود درباره خود محصول بگید
        """,
        reply_markup=keyboard
    )
    return msg


def Comment_Accepting(message, bot):
    chat_id = message.chat.id
    comment = comment_dict[chat_id]
    comment.quest_5 = message.text
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add('ثبت نظر', 'لغو و خروج')
    msg = bot.send_message(chat_id, 'نظر سنجی به اتمام رسید لطفا برای ادامه کار از دکمه های ربات استفاده کنید', reply_markup=keyboard)
    return msg


def Send_Comment(message, bot, admin_id):
    chat_id = message.chat.id
    if message.text == 'ثبت نظر':
        bot.send_message(admin_id, f"""
    نظر جدید:
    از طرف:
    {comment_dict[chat_id].info}


    کیفیت کالای خریداری شده چگونه بود؟
    {comment_dict[chat_id].quest_1}   


    سوال دوم ناموسا هیچی به ذهنم نمیرسه بگذر
    {comment_dict[chat_id].quest_2}  


    بسته بندی محصول چطور بود؟
    {comment_dict[chat_id].quest_3}  


    قیمت محصول نسبط به جاهای دیگر چطور بود؟
    {comment_dict[chat_id].quest_4}  


    نظر خود درباره خود محصول بگید
    {comment_dict[chat_id].quest_5}  


            """)
        bot.send_message(chat_id, 'نظر با موفقیت ارسال شد', reply_markup=types.ReplyKeyboardRemove())
    if message.text == 'لغو و خروج':
        bot.send_message(message.chat.id, "اوکی بای", reply_markup=types.ReplyKeyboardRemove())
