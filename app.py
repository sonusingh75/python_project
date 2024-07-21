from flask import Flask  # Import the Flask class from the flask package
from config import Config  # Import the Config class from the config module, which holds configuration settings
from extensions import db, ma  # Import the db (SQLAlchemy) and ma (Marshmallow) instances from the extensions module
from models import Employee  # Import the Employee model from the models module
from routes import main  # Import the main blueprint from the routes module
import logging  # Import the logging module to enable logging in the application

def create_app():
    app = Flask(__name__)  # Create an instance of the Flask class, which is the WSGI application

    app.config.from_object(Config)  # Load configuration settings from the Config class

    # Initialize extensions
    try:
        db.init_app(app)  # Initialize the SQLAlchemy instance with the app
        ma.init_app(app)  # Initialize the Marshmallow instance with the app
    except Exception as e:
        app.logger.error(f"Failed to initialize extensions: {e}")  # Log an error if initializing extensions fails
        raise  # Raise the exception to stop the application from running

    app.register_blueprint(main)  # Register the main blueprint with the app

    with app.app_context():  # Create an application context to work with the app
        try:
            db.create_all()  # Create all database tables defined by SQLAlchemy models
        except Exception as e:
            app.logger.error(f"Failed to create database tables: {e}")  # Log an error if creating tables fails
            raise  # Raise the exception to stop the application from running

    return app  # Return the created Flask app instance

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)  # Configure the logging to show debug level messages
    app = create_app()  # Create an instance of the Flask app using the create_app function
    app.run(debug=True)  # Run the Flask development server with debug mode enabled
