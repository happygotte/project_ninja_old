from flask import request
from flask_restx import Resource, fields, Namespace

from api.schemas.AddressSchema import AddressSchema
from api.models.Address import Address

address_schema = AddressSchema()
address_list_schema = AddressSchema(many=True)
address_ns = Namespace("address", description="Addresses")

address = address_ns.model("Address", {
    "country": fields.String("Country name"),
    "city": fields.String("City name")
})


class AddressView(Resource):

    def get(self, id):
        """Get the address"""
        address_data = Address.find_by_id(id)
        if address_data:
            response = address_schema.dump(address_data)

            return {"message": "success", "address": response}
        return {'message': "address not found"}, 404

    def delete(self, id):
        """Delete the address"""
        address_data = Address.find_by_id(id)
        if address_data:
            address_data.delete_from_db()

            return {'message': f"address {address_data.country} successfully deleted."}, 200
        return {'message': "address not found"}, 404

    @address_ns.expect(address)
    def put(self, id):
        """Update the address"""
        address_data = Address.find_by_id(id)
        address_json = request.get_json()

        if address_data:
            if address_json.get("country"):
                address_data.country = address_json["country"]
            if address_json.get("city"):
                address_data.city = address_json["city"]
        else:
            return {'message': "address not found"}, 404

        address_data.save_to_db()

        return {"message": f"address {address_data.country} successfully updated"}, 200


class AddressListView(Resource):

    def get(self):
        """Get all the addresses"""
        result = address_list_schema.dump(Address.find_all())

        return {"count": len(result), "addresses": result, "message": "success"}, 200

    @address_ns.expect(address)
    def post(self):
        """Create an address"""
        address_json = request.get_json()
        country = address_json["country"]

        if Address.find_by_country(country):
            return {'message': f"address '{country}' already exists"}, 400

        address_data = Address(country=country)
        if address_json.get("city"):
            address_data.city = address_json["city"]


        address_data.save_to_db()

        return {"message": f"address {address_data} successfully created"}, 201
