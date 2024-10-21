from lxml import etree
from pydantic import ValidationError

from src.schemes import Company


class Parser:
    """Класс парсера. Здесь происходит парсинг XML-файла и все преобразования данных."""
    def __init__(self, path: str) -> None:
        self.path = path
        self.xml = None

    def open(self) -> None:
        with open(self.path, 'rb') as f:
            self.xml = etree.parse(f).getroot()
    
    def parse(self) -> list[Company]:
        data = []
        for company in self.xml.findall('КОМПАНИЯ'):
            inn = company.find('ИНН')
            ogrn = company.find('ОГРН')
            refresh_date = company.find('ДатаОбн')
            phone = company.find('Телефон')
            name = company.find('НазваниеКомпании')
            # Проверка ОГРН на наличие в списке
            try:
                data.append(Company(
                    ogrn=str(ogrn.text),
                    inn=str(inn.text),
                    refresh_date=refresh_date.text, 
                    phone=phone.text if phone is not None else '', 
                    name=name.text if name is not None else '',
                ))
            except ValidationError as validation_error:
                self.incorrect_data(ogrn.text, inn.text)
            except ValueError as value_error:
                self.incorrect_type(ogrn.text, inn.text)

        return self.prepare_data(raw_data=data)

    def prepare_data(self, raw_data: list[Company]) -> list[tuple]:
        ready_made_data = []
        ogrn = []
        inn = []
        refresh_date = []
        phone = []
        name = []
        for company in raw_data:
            if company.ogrn not in ogrn:
                ogrn.append(company.ogrn)
                inn.append(company.inn)
                refresh_date.append(company.refresh_date)
                phone.append(self.prepare_phone(company.phone))
                name.append(company.name)
            else:
                self.ogrn_warning(company)
                idx = ogrn.index(company.ogrn)
                if company.refresh_date > refresh_date[idx]:
                    inn[idx] = company.inn
                    refresh_date[idx] = company.refresh_date
                    phone[idx] = self.prepare_phone(company.phone)
                    name[idx] = company.name
        
        ready_made_data = zip(ogrn, inn, refresh_date, phone, name)
        return ready_made_data

    def prepare_phone(self, phone: str) -> str:
        phone = phone.replace(' ', '')
        phone = phone.replace('-', '')
        phone = phone.replace('(', '')
        phone = phone.replace(')', '')
        return phone
    
    def ogrn_warning(self, company: Company) -> None:
        print(f'Внимание: обнаружено совпадение ОГРН: {company.ogrn}')

    def incorrect_data(self, ogrn: str, inn: str) -> None:
        print(f'Ошибка выполнения: данные в объекте не соответствуют требованиям. Объект: ОГРН - {ogrn}, ИНН - {inn}')

    def incorrect_type(self, ogrn: str, inn: str) -> None:
        print(f'Ошибка выполнения: некорретный тип данных. Объект: ОГРН - {ogrn}, ИНН - {inn}')