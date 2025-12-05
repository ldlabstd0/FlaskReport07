# run.py

from app import create_app, db
# Import the Config class, even though the factory will handle configuration loading
from configuration import Config 

# Create the application instance using the factory function
# We pass the Config object directly to ensure it loads correctly.
app = create_app(config_class=Config)

# --- CLI Command for Database Initialization ---
# This command registers 'flask init-db' which creates tables based on app/model.py
@app.cli.command()
def init_db():
    """Create database tables"""
    # Requires application context to access 'db'
    with app.app_context():
        # Creates all tables defined in your SQLAlchemy models (app/model.py)
        db.create_all()
    print('Database initialized.')

# --- Application Runner ---
if __name__ == '__main__':
    # Runs the development server
    app.run(debug=True)