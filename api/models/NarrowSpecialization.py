from typing import List

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import ENUM

from api.database import Base, session
from api.models.Specialization import Specialization


class NarrowSpecialization(Base):
    __tablename__ = "narrow_specialization"
    __table_args__ = {"schema": "music_schema"}

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    classification = Column(ENUM("strings", "woodwinds", "brass", "drums", "keyboards", "female voice", "ethnic",
                                 "male voice", name="classification_type"))
    diapason = Column(String)
    additional_comment = Column(String)
    specialization_id = Column(Integer, ForeignKey(Specialization.id))

    def __repr__(self):
        return f"<{__class__.__name__}: id={self.id}, " \
               f"name={self.name}, specialization_id={self.specialization_id}," \
               f"classification={self.classification}, diapason={self.diapason}," \
               f"additional_comment={self.additional_comment}>"

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()

    @classmethod
    def find_by_id(cls, _id) -> "NarrowSpecialization":
        return session.query(cls).filter_by(id=_id).first()

    @classmethod
    def find_by_name(cls, name) -> "NarrowSpecialization":
        return session.query(cls).filter_by(name=name).first()

    @classmethod
    def find_all(cls) -> List["NarrowSpecialization"]:
        return session.query(cls).all()
