from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import logging

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    with app.app_context():
        try:
            # create a connection and execute a simple query to ensure connection
            with db.engine.connect() as connection:
                connection.execute(text('SELECT 1'))
            logging.info('Database connection successful.')
        except Exception as e:
            logging.error('Error connecting to the database.')
            logging.error(e)
            raise # raise error to prevent the application from starting