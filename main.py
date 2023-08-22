from aiogram import executor
from bot_router import dp
from sys import argv
from init_db import create_tables
from utils import fill_category_data,fill_film_data


if __name__ == "__main__":
    data = argv
    print(data)
    if data[1] == "migrate":
        create_tables()
        print("Таблицы создались")
    elif data[1] == 'runbot':
        print("Бот запущен")
        executor.start_polling(dp,skip_updates=True)
    elif data[1] == 'fill_category':
        fill_category_data("data_files/category_data.csv")
        print('Заполнение таблицы категории')
    elif data[1] == 'fill_films':
        fill_film_data()
        print('Заполнение таблицы фильм')
    else:
        print("Напишите правильную команду!")
        



