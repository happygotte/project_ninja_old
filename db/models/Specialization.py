from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Specialization(Base):
    __tablename__ = "specialization"

    id = Column(Integer, primary_key=True)
    name = Column(
        ENUM("instrumental_performer", "vocalist", "composer", "conductor", "concert host", name="specialization_type"),
        nollable=False)
    characteristic_id = Column(Integer, ForeignKey("characteristic.id"))
    solo = Column(Boolean, default=False)
    characteristic = relationship("Characteristic", backref=backref("specialization"))

    def __init__(self, name, characteristic_id, solo):
        self.name = name
        self.characteristic_id = characteristic_id
        self.solo = solo

    def __repr__(self):
        return f"<{__class__.__name__}: id={self.id}, " \
               f"name={self.name}, characteristic_id={self.characteristic_id}, " \
               f"solo={self.solo}>"
