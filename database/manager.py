from database.models import Category,Film,UserGuessedFilm
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
    
    
    def get_random_film(self,film_ids,category_ids=None):
        from sqlalchemy.sql import func
        from sqlalchemy import not_
        if category_ids:
            i = self.session.query(self.model).filter(
                not_(Film.id.in_(film_ids)),
                        Film.category_id == category_ids
                    ).order_by(func.rand()).first()
            return i
        else:
            i = self.session.query(self.model).filter(
                not_(Film.id.in_(film_ids))
                ).order_by(func.rand()).first()
            return i
        
        
        

class UserGuessedFilmManager():
    
    def __init__(self) -> None:
        self.model = UserGuessedFilm
        self.session = get_session()
        
    def insert_guessed_film(self,tg_user_id,film_id):
        insert = UserGuessedFilm(
            tg_user_id = tg_user_id,
            film_id=film_id
        )
        self.session.add_all(insert)
        self.session.commit()
        
    def get_insert_guessed_film(self,tg_user_id):
        ids = self.session.query(UserGuessedFilm.id).filter(
            UserGuessedFilm.tg_user_id == tg_user_id
        )
        return ids
    
        
        


    
    


