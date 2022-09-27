from flask import request
from flask_restx import Resource, fields, Namespace

from api.schemas.FormSchema import FormSchema
from api.models.Form import Form

form_schema = FormSchema()
form_list_schema = FormSchema(many=True)    #  many=True with iterable collections of objects.
form_ns = Namespace("form", description="Musical form")

# Model for expect, will be used as a body in the Post/Put methods
form = form_ns.model("Form", {
    "name": fields.String("Name of the Form")
})


class FormView(Resource):

    def get(self, id):
        """Get the form"""
        form_data = Form.find_by_id(id)
        if form_data:
            response = form_schema.dump(form_data)

            return {"message": "success", "form": response}
        return {'message': "form not found"}, 404

    def delete(self, id):
        """Delete the form"""
        form_data = Form.find_by_id(id)
        if form_data:
            form_data.delete_from_db()

            return {'message': f"form {form_data.name} successfully deleted."}, 200
        return {'message': "form not found"}, 404

    @form_ns.expect(form)
    def put(self, id):
        """Update the form"""
        form_data = Form.find_by_id(id)
        form_json = request.get_json()

        if form_data:
            form_data.name = form_json["name"]
        else:
            return {'message': "form not found"}, 404

        form_data.save_to_db()

        return {"message": f"form {form_data.name} successfully updated"}, 200


class FormListView(Resource):

    def get(self):
        """Get all the forms"""
        result = form_list_schema.dump(Form.find_all())

        return {"count": len(result), "forms": result, "message": "success"}, 200

    @form_ns.expect(form)
    def post(self):
        """Create a form"""
        form_json = request.get_json()
        name = form_json["name"]

        if Form.find_by_name(name):
            return {'message': f"form '{name}' already exists"}, 400

        form_data = Form(name=name)
        form_data.save_to_db()

        return {"message": f"form {form_data} successfully created"}, 201
