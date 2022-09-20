from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class PerformerCollectiveRecording(Base):
    __tablename__ = "performer_collective_recording"

    musical_collective_id = Column(Integer, ForeignKey("musical_collective_id.id"), primary_key=True)
    recording_id = Column(Integer, ForeignKey("recording.id"), primary_key=True)
    musical_collective = relationship("MusicalCollective", backref=backref("performer_recording"))
    recording = relationship("Recording", backref=backref("performer_recording"))

    def __init__(self, musical_collective_id, recording_id):
        self.musical_collective_id = musical_collective_id
        self.recording_id = recording_id


    def __repr__(self):
        return f"<{__class__.__name__}: " \
               f"musical_collective_id={self.musical_collective_id}, recording_id={self.recording_id}> "