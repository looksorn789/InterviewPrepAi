from flask import Flask

#Application factory pattern naming, it allows the app to be configured
#Before it starts, to make testing easier
def create_app():
    """
    Application Factory

    Creates and configures the Flask application.
    As the project grows, this function will initialize:
    - Configuration
    - Database
    - Authentication
    - API routes
    - Extensions (SQLAlchemy, Migrate, etc.)
    """

    # Create a Flask application instance.
    # __name__ tells Flask where this package lives so it can locate
    # templates, static files, and other project resources.
    app = Flask(__name__)

    # Register the home endpoint.
    # When a client sends a GET request to "/", Flask executes home().
    @app.route("/")
    def home():
        return {"message": "InterviewPrep Ai Backend Running"}
    
    return app