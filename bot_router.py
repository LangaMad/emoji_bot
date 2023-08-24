from aiogram import Bot, Dispatcher
from bot_utils.handlers import *
from config import TOKEN

bot = Bot(token=TOKEN)

dp = Dispatcher(bot)

dp.register_message_handler(welcome_message,commands=['start'])
# dp.register_message_handler(get_movie,commands=["movie"])
dp.register_message_handler(start_game,commands=["start_game"])


dp.register_callback_query_handler(
    start_category,
    lambda c: str(c.data).startswith('category_')
)







