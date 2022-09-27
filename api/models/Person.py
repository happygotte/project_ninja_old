from typing import List

from sqlalchemy import Column, Integer, String, ForeignKey
#from sqlalchemy.orm import relationship

from api.database import Base, session
from api.models.Address import Address


class Person(Base):
    __tablename__ = "person"
    __table_args__ = {"schema": "music_schema"}

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    year_of_birth = Column(Integer)
    year_of_death = Column(Integer)
    address_id = Column(Integer, ForeignKey(Address.id))

    #musicians = relationship("Musician", backref="person")

    def __repr__(self):
        return f"<{__class__.__name__}: id={self.id}, " \
               f"first_name={self.first_name}, last_name={self.last_name}, " \
               f"year_of_birth={self.year_of_birth}, year_of_death={self.year_of_death}, " \
               f"address_id={self.address_id}>"

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()

    @classmethod
    def find_by_id(cls, _id) -> "Person":
        return session.query(cls).filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["Person"]:
        return session.query(cls).all()
