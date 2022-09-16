from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine("postgresql+psycopg2://user:password@postgresserver/db", echo=True)

Base = declarative_base()

ENUM("instrumental_performer", "vocalist", "composer", "conductor", name="specialization_type")

ENUM("strings", "woodwinds", "brass", "drums", "keyboards", "female voice", "ethnic", "male voice",
     name="classification_type")


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


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    year_of_birth = Column(Integer)
    year_of_death = Column(Integer)
    address_id = Column(Integer, ForeignKey("address.id"))
    address = relationship("Address", backref="person")

    def __init__(self, first_name, last_name, year_of_birth, year_of_death, address_id):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth  # TODO
        self.year_of_death = year_of_death  # TODO
        self.address_id = address_id  # TODO

    def __repr__(self):
        return f"<{__class__.__name__}: id={self.id}, " \
               f"first_name={self.first_name}, last_name={self.last_name}, " \
               f"year_of_birth={self.year_of_birth}, year_of_death={self.year_of_death}, " \
               f"adress_id={self.address_id}>"
        # TODO А мы можем тут сослаться на значения из другого класса, чтобы они вывелись?


class Сharacteristic(Base):
    __tablename__ = "characteristic"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    classification = Column(сlassification_type, nullable=False)
    year_of_birth = Column(Integer)
    year_of_death = Column(Integer)
    address_id = Column(Integer, ForeignKey("address.id"))
    address = relationship("Address", backref="person")

    def __init__(self, first_name, last_name, year_of_birth, year_of_death, address_id):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth  # TODO
        self.year_of_death = year_of_death  # TODO
        self.address_id = address_id  # TODO

    def __repr__(self):
        return f"<{__class__.__name__}: id={self.id}, " \
               f"first_name={self.first_name}, last_name={self.last_name}, " \
               f"year_of_birth={self.year_of_birth}, year_of_death={self.year_of_death}, " \
               f"adress_id={self.address_id}>"