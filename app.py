from flask import Flask
from extensions import db
from api.user_api import user_api
from api.claim_api import claim_api
from api.policy_api import policy_api
from api.vehicle_api import vehicle_api
from api.customer_api import customer_api
from api.address_api import address_api
from api.car_type_api import car_type_api
from api.status_api import status_api
from config import Config
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Enable Cross-Origin Resource Sharing (CORS)
    CORS(app)

    # Initialize SQLAlchemy with the app
    db.init_app(app)

    # Create tables within the app context
    with app.app_context():
        db.create_all()

    # Register all the blueprints
    app.register_blueprint(user_api)
    app.register_blueprint(claim_api)
    app.register_blueprint(policy_api)
    app.register_blueprint(vehicle_api)
    app.register_blueprint(customer_api)
    app.register_blueprint(address_api)
    app.register_blueprint(car_type_api)
    app.register_blueprint(status_api)

    return app

# Run the app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
