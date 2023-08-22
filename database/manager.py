from database.models import Category,User,Film
from db import get_session


class CategoryManager():
    def __init__(self) :
        self.model = Category
        self.session = get_session()
        
    
    def insert_category(self,data):
        inserts = []
        for i in data:
            inserts.append(
                Category(
                   name = i[0] 
                )
            )
            
        self.session.add_all(inserts)
        self.session.commit()
    
    def get_all_categories(self):
        result = self.session.query(self.model).all()
        return result
        
    
class FilmManager():
    def __init__(self) :
        self.model = Film
        self.session = get_session()
        
        
    def get_insert_film(self,data):
         insert = []
         for film in data:
            insert.append(
                Film(
                emoji_text = film[0],
                name_text = film[1],
                category_id = film[2]
                )
            )
         self.session.add_all(insert)
         self.session.commit()


    def get_films(self):
        r = self.session.query(self.model).all()
        return r


