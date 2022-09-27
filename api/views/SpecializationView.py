from flask import request
from flask_restx import Resource, fields, Namespace

from api.models.Specialization import Specialization
from api.schemas.SpecializationSchema import SpecializationSchema

spec_schema = SpecializationSchema()
spec_list_schema = SpecializationSchema(many=True)
spec_ns = Namespace("specialization", description="Musician's specialty")

spec = spec_ns.model("specialization", {
    "name": fields.String("instrumental_performer, vocalist, composer, conductor or concert host"),
    "additional_comment": fields.String("Additional information")
})


class SpecializationView(Resource):

    def get(self, id):
        """Get the specialization"""
        spec_data = Specialization.find_by_id(id)
        if spec_data:
            response = spec_schema.dump(spec_data)

            return {"message": "success", "specialization": response}
        return {'message': "specialization not found"}, 404

    def delete(self, id):
        """Delete the specialization"""
        spec_data = Specialization.find_by_id(id)
        if spec_data:
            spec_data.delete_from_db()

            return {'message': f"specialization {spec_data.name} successfully deleted."}, 200
        return {'message': "specialization not found"}, 404

    @spec_ns.expect(spec)
    def put(self, id):
        """Update the specialization"""
        spec_data = Specialization.find_by_id(id)
        spec_json = request.get_json()

        if spec_data:
            if spec_json.get("name"):
                spec_data.name = spec_json["name"]
            if spec_json.get("additional_comment"):
                spec_data.additional_comment = spec_json["additional_comment"]
        else:
            return {'message': "specialization not found"}, 404

        spec_data.save_to_db()

        return {"message": f"specialization {spec_data.name} successfully updated"}, 200


class SpecializationListView(Resource):

    def get(self):
        """Get all the specializations"""
        result = spec_list_schema.dump(Specialization.find_all())

        return {"count": len(result), "specialization": result, "message": "success"}, 200

    @spec_ns.expect(spec)
    def post(self):
        """Create a specialization"""
        spec_json = request.get_json()
        name = spec_json["name"]

        if name not in ("instrumental_performer", "vocalist", "composer", "conductor", "concert host"):
            return {'message': f"'{name}' is an invalid name"}, 400

        if Specialization.find_by_name(name):
            return {'message': f"specialization '{name}' already exists"}, 400

        spec_data = Specialization(name=name)

        if spec_json.get("additional_comment"):
            spec_data.additional_comment = spec_json["additional_comment"]

        spec_data.save_to_db()

        return {"message": f"specialization {spec_data} successfully created"}, 201
