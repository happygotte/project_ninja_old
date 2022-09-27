from typing import List

from sqlalchemy import Column, Integer, String

from api.database import Base, session


class Form(Base):
    __tablename__ = "form"
    __table_args__ = {"schema": "music_schema"}

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<{__class__.__name__}: id={self.id}, name={self.name}>"

    def save_to_db(self):
        session.add(self)
        session.commit()

    def delete_from_db(self):
        session.delete(self)
        session.commit()

    @classmethod
    def find_by_id(cls, _id) -> "Form":  # to annotate the return value for a function
        return session.query(cls).filter_by(id=_id).first()

    @classmethod
    def find_by_name(cls, name) -> "Form":
        return session.query(cls).filter_by(name=name).first()

    @classmethod
    def find_all(cls) -> List["Form"]:
        return session.query(cls).all()
