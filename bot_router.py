from aiogram import Bot, Dispatcher
from bot_utils.handlers import welcome_message,start_game,get_movie
from config import TOKEN

bot = Bot(token=TOKEN)

dp = Dispatcher(bot)

dp.register_message_handler(welcome_message,commands=['start'])
# dp.register_message_handler(get_movie,commands=["movie"])
dp.register_message_handler(start_game,commands=["game"])


dp.register_callback_query_handler()





