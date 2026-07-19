from app import create_app

# Build the Flask application using the Application Factory.
app = create_app()

# Only start the development server when this file is executed directly.
# If this file is imported by another module, the server will NOT start.
if __name__ == "__main__":
    app.run(debug=True)