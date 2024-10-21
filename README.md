## Тестовое задание ExportBase

#### Задача:
    Необходимо написать скрипт на Python для обработки XML файла с данными, их валидации и записи в реляционную базу данных.

    Проверка корректности полей:
    ОГРН: обязательное поле, состоит из 13 цифр
    ИНН: обязательное поле, состоит из 10 цифр
    Дата: обязательное поле
    Остальные поля являются необязательными

    Требования:
    В базу должны записаться только компании с корректными данными. 
    Если в файле несколько компаний с одинаковым ОГРН, необходимо сохранить только ту компанию, у которой поле "Дата" имеет наиболее позднюю дату.
    Информация о компаниях с некорректными данными или дублями ОГРН должна выводиться в консоль.

    Тип базы и структура данных на Ваш выбор.

#### Решение:
+ Python 3.12, lxml, sqlalchemy, pydantic, sqlite3
+ Установите requirements.txt, запустите main.py
+ выполните в терминале из корня sqlite3 test.db
+ в интерфейсе sql введите запрос **"SELECT * FROM company"** для того чтобы проверить, что данные записаны.
