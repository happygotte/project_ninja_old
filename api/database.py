from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg2://postgres:password@localhost/music", echo=True)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

Base = declarative_base()

