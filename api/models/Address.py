from typing import List

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from api.database import Base, session


class Address(Base):
    __tablename__ = "address"
    __table_args__ = {"schema": "music_schema"}

    id = Column(Integer, primary_key=True)
    country = Column(String, nullable=False)
    city = Column(String)

    #concert_halls = relationship("ConcertHall", backref="address")
    #musical_collectives = relationship("MusicalCollective", backref="address")
    persons = relationship("Person", backref="address")


    def __repr__(self):
        return f"<{__class__.__name__}: id={self.id}, country={self.country}, city={self.city}>"

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()

    @classmethod
    def find_by_id(cls, _id) -> "Address":
        return session.query(cls).filter_by(id=_id).first()

    @classmethod
    def find_by_country(cls, country) -> "Address":
        return session.query(cls).filter_by(country=country).first()

    @classmethod
    def find_all(cls) -> List["Address"]:
        return session.query(cls).all()
