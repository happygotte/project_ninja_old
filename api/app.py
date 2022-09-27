from flask import Flask, Blueprint
from flask_restx import Api

from api.views.AddressView import address_ns, AddressView, AddressListView
from api.views.FormView import FormView, FormListView, form_ns
from api.views.NarrowSpecializationView import narrow_ns, NarrowSpecializationView, NarrowSpecializationListView
from api.views.PersonView import person_ns, PersonView, PersonListView
from api.views.SpecializationView import spec_ns, SpecializationView, SpecializationListView

app = Flask(__name__)
bluePrint = Blueprint('api', __name__, url_prefix='/api')
api = Api(bluePrint, title='Project NINJA')
app.register_blueprint(bluePrint)


# сделать create app

@app.route('/')
def check():
    return 'Flask is working'


api.add_namespace(form_ns)
api.add_namespace(narrow_ns)
api.add_namespace(spec_ns)
api.add_namespace(address_ns)
api.add_namespace(person_ns)


form_ns.add_resource(FormView, '/<int:id>')
form_ns.add_resource(FormListView, "")
narrow_ns.add_resource(NarrowSpecializationView, '/<int:id>')
narrow_ns.add_resource(NarrowSpecializationListView, "")
spec_ns.add_resource(SpecializationView, '/<int:id>')
spec_ns.add_resource(SpecializationListView, "")
address_ns.add_resource(AddressView, '/<int:id>')
address_ns.add_resource(AddressListView, "")
person_ns.add_resource(PersonView, '/<int:id>')
person_ns.add_resource(PersonListView, "")

if __name__ == '__main__':
    app.run(debug=True)
