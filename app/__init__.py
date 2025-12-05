# __init__.py (Corrected)
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# Import the Config class directly
from configuration import Config 

db = SQLAlchemy()
migrate = Migrate()

# Pass the actual Config class object to the function
def create_app(config_class=Config): 
  app = Flask(__name__)

  # Pass the class object directly to from_object()
  app.config.from_object(config_class) 

  db.init_app(app)
  migrate.init_app(app, db)

  from app.route import main_bp
  app.register_blueprint(main_bp)

  return app