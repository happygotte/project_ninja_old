from sqlalchemy import Column, Integer, String, ForeignKey, Interval
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class MusicalComposition(Base):
    __tablename__ = "musical_composition"

    id = Column(Integer, primary_key=True)
    name = Column(String, nollable=False)
    musician_id = Column(Integer, ForeignKey("musician.id"), nollable=False)
    genre_id = Column(Integer, ForeignKey("genre.id"))
    form_id = Column(Integer, ForeignKey("form.id"))
    style_id = Column(Integer, ForeignKey("style.id"))
    tonality = Column(String)
    duration = Column(Interval) # TODO type?
    number_of_parts = Column(Integer)
    musician = relationship("Musician", backref=backref("musical_composition"))
    genre = relationship("Genre", backref=backref("musical_composition"))
    form = relationship("Form", backref=backref("musical_composition"))
    style = relationship("Style", backref=backref("musical_composition"))


    def __init__(self, name, musician_id, genre_id, form_id, style_id, tonality, duration, number_of_parts):
        self.name = name
        self.musician_id = musician_id
        self.genre_id = genre_id
        self.form_id = form_id
        self.style_id = style_id
        self.tonality = tonality
        self.duration = duration
        self.number_of_parts = number_of_parts

    def __repr__(self):
        return f"<{__class__.__name__}: id={self.id}, " \
               f"name={self.name}, musician_id={self.musician_id}, " \
               f"genre_id={self.genre_id}, form_id={self.form_id}, style_id={self.style_id}, " \
               f"tonality={self.tonality}, duration={self.duration}, number_of_parts={self.number_of_parts}>"
