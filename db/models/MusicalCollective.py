from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class MusicalCollective(Base):
    __tablename__ = "musical_collective"

    id = Column(Integer, primary_key=True)
    name = Column(String, nollable=False)
    type_collective = Column(String)
    number_of_members = Column(Integer)
    address_id = Column(Integer, ForeignKey("address.id"))
    address = relationship("Address", backref=backref("musical_collective"))

    def __init__(self, name, type_collective, number_of_members, address_id):
        self.name = name
        self.type_collective = type_collective
        self.number_of_members = number_of_members
        self.address_id = address_id

    def __repr__(self):
        return f"<{__class__.__name__}: id={self.id}, " \
               f"name={self.name}, type_collective={self.type_collective}, " \
               f"number_of_members={self.number_of_members}, address_id={self.address_id}>"
