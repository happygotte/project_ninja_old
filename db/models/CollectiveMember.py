from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class CollectiveMember(Base):
    __tablename__ = "collective_member"

    musical_collective_id = Column(Integer, ForeignKey("musical_collective.id"), primary_key=True)
    musician_id = Column(Integer, ForeignKey("musician.id"), primary_key=True)
    musical_collective = relationship("Musical_collective", backref=backref("collective_member"))
    musician = relationship("Musician", backref=backref("collective_member"))

    def __init__(self, musical_collective_id, musician_id):
        self.musical_collective_id = musical_collective_id
        self.musician_id = musician_id

    def __repr__(self):
        return f"<{__class__.__name__}: " \
               f"musical_collective_id={self.musical_collective_id}, musician_id={self.musician_id}> "
