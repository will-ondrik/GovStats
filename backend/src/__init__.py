import os
from dotenv import load_dotenv
import logging
from flask import Flask
from flask_cors import CORS
from src.database.db import init_db
from src.controllers.authentication.authentication_controller import AuthenticationController
from src.controllers.house.house_controller import HouseController
from src.controllers.members.members_controller import MembersController
from src.controllers.party.party_controller import PartyController

# Load environment variables
load_dotenv()

# Print the database URI to verify it's loaded correctly
print(os.getenv('SQLALCHEMY_DATABASE_URI'))

# Create the database config dictionary
db_config = {
    'SQLALCHEMY_DATABASE_URI': os.getenv('SQLALCHEMY_DATABASE_URI'),
    'SQLALCHEMY_TRACK_MODIFICATIONS': os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', 'False').lower() in ('true', '1', 't')
}

def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    # Update the app config with the database config
    app.config.update(db_config)

    if test_config is None:
        # Load the instance config, if it exists
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config
        app.config.update(test_config)
    
    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize logging
    logging.basicConfig(level=logging.INFO)

    # Initialize the database
    init_db(app)

    # Create instances of controllers
    auth_controller = AuthenticationController()
    house_controller = HouseController()
    members_controller = MembersController()
    party_controller = PartyController()

    # Register blueprints
    app.register_blueprint(auth_controller.blueprint, url_prefix=f'/{auth_controller.base_path}')
    app.register_blueprint(house_controller.blueprint, url_prefix=f'/{house_controller.base_path}')
    app.register_blueprint(members_controller.blueprint, url_prefix=f'/{members_controller.base_path}')
    app.register_blueprint(party_controller.blueprint, url_prefix=f'/{party_controller.base_path}')

    @app.route('/hello')
    def hello():
        return 'Hello, world'

    return app
