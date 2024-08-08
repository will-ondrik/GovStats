import os
from dotenv import load_dotenv
import logging
from flask import Flask
from src.database.db import init_db
from src.controllers.authentication.authentication_controller import Authentication_Controller
from src.controllers.members.members_controller import Members_Controller

# load env and extract values
load_dotenv()

db_config = {
    'SQLALCHEMY_DATABASE_URI': os.getenv('SQLALCHEMY_DATABASE_URI'),
    'SQLALCHEMY_TRACK_MODIFICATIONS': os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
}


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(db_config)

    if test_config is None:
        # load the instance config, if exists
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config
        app.config.update(test_config)
    
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    # initializing logging
    logging.basicConfig(level=logging.INFO)
    # init db
    init_db(app)

    # create instances of controllers
    auth_controller = Authentication_Controller()
    members_controller = Members_Controller()

    # register blueprints
    app.register_blueprint(auth_controller.router, url_prefix=f'/{auth_controller.base_path}')
    app.register_blueprint(members_controller.router, url_prefix=f'/{members_controller.base_path}')


    @app.route('/hello')
    def hello():
        return 'Hello, world'

    return app