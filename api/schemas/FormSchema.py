from api.ma import ma
from api.models.Form import Form


class FormSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Form
        include_relationships = True
        load_instance = True  # Optional: deserialize to model instances
