from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    country = Column(String, nullable=False)
    city = Column(String)

    def __init__(self, country, city):
        self.country = country
        self.city = city  # TODO Если не not null, то должно ли это быть в конструкторе? Или по умолчанию null?

    def __repr__(self):
        return f"<{__class__.__name__}: id={self.id}, country={self.country}, city={self.city}>"
