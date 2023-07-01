from Handlers import Start_Handler
from Quests import Quest1, Quest2, Quest3, Quest4, Quest5
from Quests import Comment_Accepting, Send_Comment
from telebot import TeleBot
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('bot_token')
bot = TeleBot(token)

# Admin ID
admin_id = 1713227576


@bot.message_handler(commands=['start'])
def start_handler(message):
    Start_Handler(message, bot)


@bot.callback_query_handler(func=lambda call: call.data)
def callback_query(call):
    bot.send_message(call.from_user.id, """
        در این نظر سنجی 5 سوال از شما پرسیده میشود
        پاسخ های شما با کسی به غیر از ادمین به اشتراک گذاشته نمیشود
        پس از شروع نظر سنجی دکمه هایی برای ثبت نظر در ربات قرار میگیرد برای ثبت نظر خود از این دکمه ها استفاده کنید
            """)
    msg = bot.send_message(
        call.from_user.id,
        'لطفا نام و نام خانوادگی خود را وارد کنید:'
    )
    if call.data == 'commenting':
        bot.register_next_step_handler(msg, process_stepOne)


def process_stepOne(message):
    msg = Quest1(message, bot)
    bot.register_next_step_handler(msg, process_stepTwo)


def process_stepTwo(message):
    msg = Quest2(message, bot)
    bot.register_next_step_handler(msg, process_stepThree)


def process_stepThree(message):
    msg = Quest3(message, bot)
    bot.register_next_step_handler(msg, process_stepFour)


def process_stepFour(message):
    msg = Quest4(message, bot)
    bot.register_next_step_handler(msg, process_stepFive)


def process_stepFive(message):
    msg = Quest5(message, bot)
    bot.register_next_step_handler(msg, process_stepSix)


def process_stepSix(message):
    msg = Comment_Accepting(message, bot)
    bot.register_next_step_handler(msg, process_finally)


def process_finally(message):
    Send_Comment(message, bot, admin_id)


bot.infinity_polling()
