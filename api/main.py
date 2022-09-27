from api.database import session
from api.models.NarrowSpecialization import NarrowSpecialization
from api.models.Specialization import Specialization

#new_rec = Form(name="Simple three-part form")

ex2 = NarrowSpecialization(name="oboe", classification="woodwinds")
ex1 = session.query(Specialization).filter(Specialization.id == 1).first()
ex1.narrow_specializations.append(ex2)


session.add(ex2)
session.add(ex1)
session.commit()


