from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class ConcertHall(Base):
    __tablename__ = "concert_hall"

    id = Column(Integer, primary_key=True)
    name = Column(String, nollable=False)
    number_of_seats = Column(Integer)
    address_id = Column(Integer, ForeignKey("address.id"))
    address = relationship("Address", backref=backref("concert_hall"))

    def __init__(self, name, number_of_seats, address_id):
        self.name = name
        self.number_of_seats = number_of_seats
        self.address_id = address_id

    def __repr__(self):
        return f"<{__class__.__name__}: id={self.id}, " \
               f"name={self.name}, number_of_seats={self.number_of_seats}, " \
               f"address_id={self.address_id}>"
