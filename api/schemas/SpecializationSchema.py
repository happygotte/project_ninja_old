from api.ma import ma
from api.models.Specialization import Specialization
from api.schemas.NarrowSpecializationSchema import NarrowSpecializationSchema


class SpecializationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Specialization
        include_relationships = True
        load_instance = True

    narrow_specializations = ma.Nested(NarrowSpecializationSchema, many=True)


