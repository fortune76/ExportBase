from pydantic import BaseModel, field_validator
from datetime import date

class Company(BaseModel):
    ogrn: str
    inn: str
    refresh_date: date
    phone: str = None
    name: str = None

    @field_validator('ogrn')
    @classmethod
    def validate_ogrn(cls, v: str) -> str:
        if len(v) != 13:
            raise ValueError('ОГРН содержит неверное количество цифр.')
        if not v.isdigit():
            raise ValueError('ОГРН содержит неверные символы.')

        return v

    @field_validator('inn')
    @classmethod
    def validate_inn(cls, v: str) -> str:
        if len(v) != 10:
            raise ValueError('ИНН содержит неверное количество цифр.')
        if not v.isdigit():
            raise ValueError('ИНН содержит неверные символы.')
        return v
