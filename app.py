from flask import Flask
from models.user import db
from api.user_api import user_api
from config import Config
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)

db.init_app(app)

with app.app_context():
    db.create_all()  # Create tables

app.register_blueprint(user_api)

if __name__ == '__main__':
    app.run(debug=True)
