from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config.from_object(os.environ["APP_SETTINGS"])  # TODO надо ли
app.config[
    'SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Поскольку мы не создаём программу, управляемую событиями, а эта функция включена по умолчанию
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:password@localhost/music"

db = SQLAlchemy(app)  # TODO надо ли
ma = Marshmallow(app)  # TODO если я решу делать схемы

if __name__ == "__main__":
    db.init_app(app) # TODO надо ли
    app.run(debug=True)
