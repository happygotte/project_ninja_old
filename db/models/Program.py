from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Program(Base):
    __tablename__ = "program"

    musical_composition_id = Column(Integer, ForeignKey("musical_composition.id"), primary_key=True)
    concert_id = Column(Integer, ForeignKey("concert.id"), primary_key=True)
    musical_composition = relationship("MusicalComposition", backref=backref("program"))
    concert = relationship("Concert", backref=backref("program"))

    def __init__(self, musical_composition_id, concert_id):
        self.musical_composition_id = musical_composition_id
        self.concert_id = concert_id

    def __repr__(self):
        return f"<{__class__.__name__}: " \
               f"musical_composition_id={self.musical_composition_id}, concert_id={self.concert_id}>"
