#from app import db
#from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker

Base = declarative_base()

class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    country = Column(String, nullable=False)
    city = Column(String)

    def __init__(self, country, city):
        self.country = country
        self.city = city  # TODO Если не not null, то должно ли это быть в конструкторе? Или по умолчанию null?

    def __repr__(self):
        return f"<{__class__.__name__}: id={self.id}, country={self.country}, city={self.city}>"

def main():
    engine = create_engine("postgresql+psycopg2://postgres:password@localhost/postgres", echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    ex_address1 = Address(country="Canada", city="Ottawa")
    ex_address2 = Address(country="Chile", city="Santiago")

    session.add(ex_address1)
    session.add(ex_address2)

    session.commit()

    for ex in session.query(Address):
        print(ex)

if __name__=="__main__":
    main()



