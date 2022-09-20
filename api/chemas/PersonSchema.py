# we need to setup the schema for our model.
# This is necessary because we want to parse our post object(s) into a JSON response
from api.app import ma


class PersonSchema(ma.Schema):
    class Meta:
        fields = (
            "first_name",
            "last_name",
            "year_of_birth",
            "year_of_death",
            "address_id",
            "address"
        )
