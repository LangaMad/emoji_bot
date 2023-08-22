import csv 
from database.manager import CategoryManager,FilmManager

def fill_category_data(filename):
    with open(filename,"r",encoding="utf-8") as csv_file:
        rows = csv.reader(csv_file,delimiter=",")
        CategoryManager().insert_category(rows)


def fill_film_data():
    with open("data_files/film_data.csv","r",encoding="utf-8") as file:
        rows = csv.reader(file,delimiter=",")
        FilmManager().get_insert_film(data=rows)
        
        

            







