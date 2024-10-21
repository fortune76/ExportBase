from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Database:
    """Класс базы данных. Здесь настраивается подключение. Использовал sqlite как самую простую бд"""
    def __init__(self, db_path: str) -> None:
        self.engine = None
        self.session = None
        self.db_path = db_path

    def connect(self) -> None:
        self.engine = create_engine('sqlite:///' + self.db_path + '/test.db')
        self.session = sessionmaker(bind=self.engine)

    def disconnect(self) -> None:
        self.engine.dispose()
