from typing import List

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import relationship
from api.database import Base, session


class Specialization(Base):
    __tablename__ = "specialization"
    __table_args__ = {"schema": "music_schema"}

    id = Column(Integer, primary_key=True)
    name = Column(
        ENUM("instrumental_performer", "vocalist", "composer", "conductor", "concert host", name="specialization_type"),
        nullable=False)
    additional_comment = Column(String)

    narrow_specializations = relationship("NarrowSpecialization", backref="specialization")

    # musicians = relationship('Musician', backref='specialization')

    def __repr__(self):
        return f"<{__class__.__name__}: id={self.id}, " \
               f"name={self.name}, additional_comment={self.additional_comment}>"

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()

    @classmethod
    def find_by_id(cls, _id) -> "Specialization":
        return session.query(cls).filter_by(id=_id).first()

    @classmethod
    def find_by_name(cls, name) -> "Specialization":
        return session.query(cls).filter_by(name=name).first()

    @classmethod
    def find_all(cls) -> List["Specialization"]:
        return session.query(cls).all()
