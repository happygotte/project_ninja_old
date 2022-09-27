from api.ma import ma
from api.models.Person import Person


class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        include_relationships = True
        load_instance = True
