from api.ma import ma
from api.models.NarrowSpecialization import NarrowSpecialization


class NarrowSpecializationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = NarrowSpecialization
        include_relationships = True
        load_instance = True

