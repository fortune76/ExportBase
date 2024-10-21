import os
from src.app import App

if __name__ == '__main__':
    app = App('companies.xml', os.getcwd())
    app.parse()
    app.insert_to_db()
