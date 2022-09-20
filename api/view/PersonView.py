from flask import request, jsonify

from api.app import db, app
from api.chemas.PersonSchema import PersonSchema
from db.models.Person import Person


class PersonView:

    @app.route("/person", methods=["POST", "GET"])
    def handle_persons(self):
        if request.method == "POST":
            if request.is_json:
                first_name = request.json["first_name"]
                # или  data = request.get_json(),
                # т.е. берём сразу всё и потом устанавливаем в объект типа
                # new_person = Person(first_name=data['first_name'], last_name=data['last_name'], ...)
                last_name = request.json["last_name"]
                year_of_birth = request.json["year_of_birth"]
                year_of_death = request.json["year_of_death"]
                address_id = request.json["address_id"]

                new_person = Person(first_name, last_name, year_of_birth, year_of_death, address_id)

                db.session.add(new_person)
                db.session.commit()

                # return jsonify(new_person) # если надо вернуть общий вид
                return {"message": f"car {new_person.name} has been created successfully."}
            else:
                return {"error": "The request payload is not in JSON format"}

        elif request.method == "GET":
            person_schema = PersonSchema()

            persons = Person.query.all()
            result = person_schema.dump(persons)

            # return jsonify(result)
            return {"count": len(result), "persons": result, "message": "success"}

    app.root("/person/<id>", methods=["GET", "PUT", "DELETE"])

    def handle_person(self, id):
        person = Person.query.get_or_404(id)
        person_schema = PersonSchema()

        if request.method == "GET":
            response = person_schema.dump(person)

            # return jsonify(response)
            return {"message": "success", "person": response}

        elif request.method == "PUT":
            data = request.get_json()

            person.first_name = data["first_name"]
            person.last_name = data["last_name"]
            person.year_of_birth = data["year_of_birth"]
            person.year_of_death = data["year_of_death"]
            person.address_id = data["address_id"]

            db.session.add(person)
            db.session.commit()

            # return person_schema.jsonify(person)
            return {"message": f"car {person.name} successfully updated"}

        elif request.method == "DELETE":
            db.session.delete(person)
            db.session.commit()

            return {"message": f"Car {person.name} successfully deleted."}





