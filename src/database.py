from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Database:
    """Класс базы данных. Здесь настраивается подключение. Использовал sqlite как самую простую бд"""
    def __init__(self) -> None:
        self.engine = None
        self.session = None

    def connect(self) -> None:
        self.engine = create_engine('sqlite:////home/fortune/ExportBase/test.db')
        self.session = sessionmaker(bind=self.engine)

    def disconnect(self) -> None:
        self.engine.dispose()
