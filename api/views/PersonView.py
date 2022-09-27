from flask import request
from flask_restx import Resource, fields, Namespace

from api.models.Person import Person
from api.schemas.PersonSchema import PersonSchema

person_schema = PersonSchema()
person_list_schema = PersonSchema(many=True)
person_ns = Namespace("person",
                      description="Participant in musical activity")

person = person_ns.model("person", {
    "first_name": fields.String("Person's first name"),
    "last_name": fields.String("Person's last name"),
    "year_of_birth": fields.Integer("Person's year of birth "),
    "year_of_death": fields.Integer("Person's year of death"),
    "address_id": fields.Integer("Residential address")
})


class PersonView(Resource):

    def get(self, id):
        """Get the person"""
        person_data = Person.find_by_id(id)
        if person_data:
            response = person_schema.dump(person_data)

            return {"message": "success", "person": response}
        return {'message': "person not found"}, 404

    def delete(self, id):
        """Delete the person"""
        person_data = Person.find_by_id(id)
        if person_data:
            person_data.delete_from_db()

            return {'message': f"person {person_data.first_name} {person_data.last_name} successfully deleted."}, 200
        return {'message': "person not found"}, 404

    @person_ns.expect(person)
    def put(self, id):
        """Update the person"""
        person_data = Person.find_by_id(id)
        person_json = request.get_json()

        if person_data:
            if person_json.get("first_name"):
                person_data.first_name = person_json["first_name"]
            if person_json.get("last_name"):
                person_data.last_name = person_json["last_name"]
            if person_json.get("year_of_birth"):
                person_data.year_of_birth = person_json["year_of_birth"]
            if person_json.get("year_of_death"):
                person_data.year_of_death = person_json["year_of_death"]
            if person_json.get("address_id"):
                person_data.address_id = person_json["address_id"]
        else:
            return {'message': "person specialization not found"}, 404

        person_data.save_to_db()

        return {"message": f"person {person_data.first_name} {person_data.last_name} successfully updated"}, 200


class PersonListView(Resource):

    def get(self):
        """Get all the person"""
        result = person_list_schema.dump(Person.find_all())

        return {"count": len(result), "person": result, "message": "success"}, 200

    @person_ns.expect(person)
    def post(self):
        """Create a person"""
        person_json = request.get_json()
        first_name = person_json["first_name"]
        last_name = person_json["last_name"]

        person_data = Person(first_name=first_name, last_name=last_name)

        if person_json.get("year_of_birth"):
            person_data.year_of_birth = person_json["year_of_birth"]
        if person_json.get("year_of_death"):
            person_data.year_of_death = person_json["year_of_death"]
        if person_json.get("address_id"):
            person_data.address_id = person_json["address_id"]

        person_data.save_to_db()

        return {"message": f"person {person_data} successfully created"}, 201
