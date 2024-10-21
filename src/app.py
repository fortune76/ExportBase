from sqlite3 import IntegrityError

from src.database import Database
from src.parser import Parser
from src.models import CompanyModel

class App:
    """Класс приложения. 
    Не стал выносить логику работы с базой в отдельный модуль, т.к. используется всего 1 запрос."""
    def __init__(self, path: str) -> None:
        self.parser = Parser(path)
        self.db = Database()
        self.data = None
    
    def parse(self) -> None:
        self.parser.open()
        self.data = self.parser.parse()

    def insert_to_db(self) -> None:
        self.db.connect()
        try:
            with self.db.session() as session:
                companies = [CompanyModel(
                    ogrn=company[0],
                    inn=company[1],
                    refresh_date=company[2],
                    phone=company[3],
                    name=company[4],
                    ) for company in self.data]
                session.add_all(companies)
                session.commit()
        except Exception as e:
            print('Ошибка при добавлении данных в базу.')

        self.db.disconnect()
