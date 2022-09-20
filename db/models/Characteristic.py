from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Characteristic(Base):
    __tablename__ = "characteristic"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    classification = Column(ENUM("strings", "woodwinds", "brass", "drums", "keyboards", "female voice", "ethnic",
                                 "male voice", name="classification_type"), nullable=False)
    diapason = Column(String)
    additional_comment = Column(String)

    def __init__(self, name, classification, diapason, additional_comment):
        self.name = name
        self.classification = classification
        self.diapason = diapason
        self.additional_comment = additional_comment

    def __repr__(self):
        return f"<{__class__.__name__}: id={self.id}, " \
               f"name={self.name}, classification={self.classification}, " \
               f"diapason={self.diapason}, additional_comment={self.additional_comment}>"
