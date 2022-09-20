from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Musician(Base):
    __tablename__ = "musician"

    id = Column(Integer, primary_key=True)
    specialization_id = Column(Integer, ForeignKey("specialization.id"), nollable=False)
    person_id = Column(Integer, ForeignKey("person.id"), nollable=False)
    specialization = relationship("Specialization", backref=backref("musician"))
    person = relationship("Person", backref=backref("musician"))

    def __init__(self, specialization_id, person_id):
        self.specialization_id = specialization_id
        self.person_id = person_id

    def __repr__(self):
        return f"<{__class__.__name__}: id={self.id}, " \
               f"specialization_id={self.specialization_id}, person_id={self.person_id}>"
