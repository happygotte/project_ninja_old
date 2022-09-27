from api.ma import ma
from api.models.Address import Address
from api.schemas.PersonSchema import PersonSchema


class AddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Address
        include_relationships = True
        load_instance = True

    persons = ma.Nested(PersonSchema, many=True)
