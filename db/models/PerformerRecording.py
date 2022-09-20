from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class PerformerRecording(Base):
    __tablename__ = "performer_recording"

    musician_id = Column(Integer, ForeignKey("musician.id"), primary_key=True)
    recording_id = Column(Integer, ForeignKey("recording.id"), primary_key=True)
    musician = relationship("Musician", backref=backref("performer_recording"))
    recording = relationship("Recording", backref=backref("performer_recording"))

    def __init__(self, musician_id, recording_id):
        self.musician_id = musician_id
        self.recording_id = recording_id


    def __repr__(self):
        return f"<{__class__.__name__}: " \
               f"musician_id={self.musician_id}, recording_id={self.recording_id}> "