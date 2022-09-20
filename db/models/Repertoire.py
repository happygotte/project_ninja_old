from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Repertoire(Base):
    __tablename__ = "repertoire"

    musical_composition_id = Column(Integer, ForeignKey("musical_composition.id"), primary_key=True)
    musician_id = Column(Integer, ForeignKey("musician.id"), primary_key=True)
    musical_composition = relationship("MusicalComposition", backref=backref("repertoire"))
    musician = relationship("Musician", backref=backref("repertoire"))

    def __init__(self, musical_composition_id, concert_id):
        self.musical_composition_id = musical_composition_id
        self.concert_id = concert_id

    def __repr__(self):
        return f"<{__class__.__name__}: " \
               f"musical_composition_id={self.musical_composition_id}, musician_id={self.musician_id}>"
