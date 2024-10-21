from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column
from sqlalchemy import String, Date

class Base(DeclarativeBase):
    pass

class CompanyModel(Base):
    __tablename__ = 'company'

    ogrn = Column(String(13), primary_key=True)
    inn = Column(String(10), nullable=False)
    refresh_date = Column(Date, nullable=False)
    phone = Column(String(32), nullable=True)
    name = Column(String(64), nullable=True)
