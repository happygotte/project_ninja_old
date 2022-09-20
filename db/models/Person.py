from sqlalchemy import Column, Integer, String, ForeignKey, MetaData, Table
from sqlalchemy.orm import mapper, relationship, declarative_base, backref

Base = declarative_base()


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nollable=False)
    last_name = Column(String, nollable=False)
    year_of_birth = Column("year_of_birth", Integer),
    year_of_death = Column("year_of_death", Integer),
    address_id = Column("address_id", Integer, ForeignKey("address.id"))
    address = relationship("Address", backref=backref("person"))

    def __init__(self, first_name, last_name, year_of_birth, year_of_death, address_id):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.year_of_death = year_of_death
        self.address_id = address_id

    def __repr__(self):
        return f"<{__class__.__name__}: id={self.id}, " \
               f"first_name={self.first_name}, last_name={self.last_name}, " \
               f"year_of_birth={self.year_of_birth}, year_of_death={self.year_of_death}, " \
               f"address_id={self.address_id}>"
