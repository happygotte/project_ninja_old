from flask import request
from flask_restx import Resource, fields, Namespace

from api.models.NarrowSpecialization import NarrowSpecialization
from api.schemas.NarrowSpecializationSchema import NarrowSpecializationSchema

narrow_schema = NarrowSpecializationSchema()
narrow_list_schema = NarrowSpecializationSchema(many=True)
narrow_ns = Namespace("narrow specialization",
                      description="Types of specialization (musical instrument, voice, type of conducting)")

narrow = narrow_ns.model("narrow specialization", {
    "name": fields.String("Name of the narrow specialization"),
    "classification": fields.String("For musical instrument or voice "
                                    "(strings, woodwinds, brass, drums, keyboards, ethnic, female voice or male voice)"),
    "diapason": fields.String("For musical instrument or voice"),
    "additional_comment": fields.String("For example, a member of the instrument family"),
    "specialization_id": fields.Integer
})


class NarrowSpecializationView(Resource):

    def get(self, id):
        """Get the narrow specialization"""
        narrow_data = NarrowSpecialization.find_by_id(id)
        if narrow_data:
            response = narrow_schema.dump(narrow_data)

            return {"message": "success", "narrow specialization": response}
        return {'message': "narrow specialization not found"}, 404

    def delete(self, id):
        """Delete the narrow specialization"""
        narrow_data = NarrowSpecialization.find_by_id(id)
        if narrow_data:
            narrow_data.delete_from_db()

            return {'message': f"narrow specialization {narrow_data.name} successfully deleted."}, 200
        return {'message': "narrow specialization not found"}, 404

    @narrow_ns.expect(narrow)
    def put(self, id):
        """Update the narrow specialization"""
        narrow_data = NarrowSpecialization.find_by_id(id)
        narrow_json = request.get_json()

        if narrow_data:
            if narrow_json.get("name"):
                narrow_data.name = narrow_json["name"]
            if narrow_json.get("classification"):
                narrow_data.classification = narrow_json["classification"]
            if narrow_json.get("diapason"):
                narrow_data.diapason = narrow_json["diapason"]
            if narrow_json.get("additional_comment"):
                narrow_data.additional_comment = narrow_json["additional_comment"]
            if narrow_json.get("specialization_id"):
                narrow_data.specialization_id = narrow_json["specialization_id"]
        else:
            return {'message': "narrow specialization not found"}, 404

        narrow_data.save_to_db()

        return {"message": f"narrow specialization {narrow_data.name} successfully updated"}, 200


class NarrowSpecializationListView(Resource):

    def get(self):
        """Get all the narrow specializations"""
        result = narrow_list_schema.dump(NarrowSpecialization.find_all())

        return {"count": len(result), "narrow specialization": result, "message": "success"}, 200

    @narrow_ns.expect(narrow)
    def post(self):
        """Create a narrow specialization"""
        narrow_json = request.get_json()
        name = narrow_json["name"]

        #narrow_data = narrow_schema.load(narrow_json)

        narrow_data = NarrowSpecialization(name=name)

        if narrow_json.get("classification"):
            narrow_data.classification = narrow_json["classification"]
        if narrow_json.get("diapason"):
            narrow_data.diapason = narrow_json["diapason"]
        if narrow_json.get("additional_comment"):
            narrow_data.additional_comment = narrow_json["additional_comment"]
        if narrow_json.get("specialization_id"):
            narrow_data.specialization_id = narrow_json["specialization_id"]

        narrow_data.save_to_db()

        return {"message": f"narrow specialization {narrow_data} successfully created"}, 201
