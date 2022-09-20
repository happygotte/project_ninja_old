from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Recording(Base):
    __tablename__ = "recording"

    id = Column(Integer, primary_key=True)
    musical_composition_id = Column(Integer, ForeignKey("form.id"), nullable=False)
    date = Column(Integer)
    additional_comment = Column(String)
    style = relationship("MusicalComposition", backref=backref("recording"))


    def __init__(self, musical_composition_id, date, additional_comment):
        self.musical_composition_id = musical_composition_id
        self.date = date
        self.additional_comment = additional_comment

    def __repr__(self):
        return f"<{__class__.__name__}: id={self.id}, " \
               f"name={self.musical_composition_id}, classification={self.musical_composition_id}, " \
               f"date={self.date}, additional_comment={self.additional_comment}>"
