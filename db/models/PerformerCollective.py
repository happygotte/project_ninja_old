from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class PerformerCollective(Base):
    __tablename__ = "performer_collective"

    musical_collective_id = Column(Integer, ForeignKey("musical_collective_id.id"), primary_key=True)
    concert_id = Column(Integer, ForeignKey("concert.id"), primary_key=True)
    musical_collective = relationship("MusicalCollective", backref=backref("performer_collective"))
    concert = relationship("Concert", backref=backref("performer_collective"))

    def __init__(self, musical_collective_id, concert_id):
        self.musical_collective_id = musical_collective_id
        self.concert_id = concert_id


    def __repr__(self):
        return f"<{__class__.__name__}: " \
               f"musical_collective_id={self.musical_collective_id}, concert_id={self.concert_id}> "