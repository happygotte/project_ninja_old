from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, MetaData, Table

metadata = MetaData()

engine = create_engine("postgresql+psycopg2://postgres:password@localhost/postgres", echo=True)

person = Table("person", metadata,
               Column("id", Integer, primary_key=True),
               Column("first_name", String, nullable=False),
               Column("last_name", String, nullable=False),
               Column("year_of_birth", Integer),
               Column("year_of_death", Integer),
               Column("address_id", Integer, ForeignKey("address.id"))
               )

metadata.create_all(engine)
