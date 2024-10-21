from src.app import App

if __name__ == '__main__':
    app = App('companies.xml')
    app.parse()
    app.insert_to_db()
