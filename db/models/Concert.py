from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Concert(Base):
    __tablename__ = "concert"

    id = Column(Integer, primary_key=True)
    name = Column(String, nollable=False)
    date = Column(Integer)
    ticket_price = Column(Numeric)
    concert_hall_id = Column(Integer, ForeignKey("concert_hall.id"))
    concert_hall = relationship("ConcertHall", backref=backref("concert"))

    def __init__(self, name, date, concert_hall_id, ticket_price):
        self.name = name
        self.date = date
        self.concert_hall_id = concert_hall_id
        self.ticket_price = ticket_price

    def __repr__(self):
        return f"<{__class__.__name__}: id={self.id}, " \
               f"date={self.date}, concert_hall_id={self.concert_hall_id}, " \
               f"ticket_price={self.ticket_price}>"
