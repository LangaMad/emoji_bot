from aiogram import types
from database.manager import CategoryManager,FilmManager,UserGuessedFilmManager
from bot_utils.keyboards import get_category_btns
from redis_client import redis_client
from aiogram.dispatcher import FSMContext
from .states import UserMessageState

async def welcome_message(message:types.Message):
    text = """
        Привет , я бот для игры в угадай фильм по эмоджи.
        \nЧто бы начать игру, отправь мне сообщение 
        \n/start_game
    """
    await message.answer(text)
    
    
async def start_game(message:types.Message ):
    text = "Выберите категорию игры"
    user_id = message['from'].id
    
    data = await redis_client.get_user_data(user_tg_id=user_id)
    
    if data:
        await message.answer('Вы уже в игре. Желаете завершить игру?')
    else:
        markup = get_category_btns()
        await message.answer(text,reply_markup=markup)
    
    
    
def get_random_film(tg_id,category_id):
    guessed_film = UserGuessedFilmManager().get_insert_guessed_film(tg_id)
    film = FilmManager().get_random_film(film_ids=guessed_film,category_ids=category_id)
    return film
    

async def finish_game(message:types.Message):   
    user_id = message['from'].id
    await redis_client.del_user_data(user_id)
    await message.answer('Игра завершена')
    await message.answer('Количество правильных ответов: 0')
    




async def start_category(call: types.CallbackQuery, state: FSMContext):
    user_data = await redis_client.get_user_data(call.message.chat.id)
    if user_data:
        text = '''
                У вас уже есть актниваня игра. Завершите ее чтобы продолжить
        '''
        await call.message.answer(text)
    else:
        
        choice = str(call.data).split('_')[1]
        data ={
            'level_choice':choice,
            'test':'test'
        }
    
        user_id = call.message.chat.id
        await redis_client.cache_user_data(user_tg_id=user_id,data=data)
        tg_id = user_id
        guessed_film = UserGuessedFilmManager().get_insert_guessed_film(tg_id)
        film = FilmManager().get_random_film(film_ids=guessed_film,category_ids=choice)
        await redis_client.cache_user_film(tg_id,{"id":film.id,"text":film.name_text})
        await call.message.answer('Вы выбрали категорию игры,Игра началась')
        await call.message.answer(f'{film.emoji_text}')

import pickle

async def send_question(message:types.Message, state:FSMContext):
    tg_id = message['from'].id
    user_data = await redis_client.get_user_data(tg_id)
    if user_data:
        answer = message.text
        user_film = await redis_client.get_user_film(tg_id)
        print(user_film)
        # encode_film = user_film['text'].decode("utf-8")
        # print(encode_film)
        if answer == user_film['text'] :
            await message.answer("Вы ответили верно!")
            await redis_client.delete_user_film(tg_id)
            UserGuessedFilmManager.insert_guessed_film(tg_user_id=tg_id,film_id=user_film['id'])
            film = get_random_film(tg_id,category_id=user_data["level_choice"])
            redis_client.cache_user_film(tg_id,{"id":film.id,"text":film.name_text})
            await message.answer("Угадай следующий фильм")
            await message.answer(f'{film.emoji_text}')
        else:
            await message.answer("Вы не угадали назавание попробуйте еще")
    else:
        await message.answer("У вас нет активной игры  \n нажмите /start_game чтобы начать ")
      

async def get_movie(message:types.Message):
    films = FilmManager().get_films()
    for f in films:
        await message.answer(f"{f.emoji_text}")
        
        
    
    




