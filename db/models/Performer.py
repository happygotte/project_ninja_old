from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Performer(Base):
    __tablename__ = "performer"

    musician_id = Column(Integer, ForeignKey("musician.id"), primary_key=True)
    concert_id = Column(Integer, ForeignKey("concert.id"), primary_key=True)
    musician = relationship("Musician", backref=backref("performer"))
    concert = relationship("Concert", backref=backref("performer"))

    def __init__(self, musician_id, concert_id):
        self.musician_id = musician_id
        self.concert_id = concert_id

    def __repr__(self):
        return f"<{__class__.__name__}: " \
               f"musician_id={self.musician_id}, concert_id={self.concert_id}>"
