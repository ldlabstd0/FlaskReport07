from app import create_app, db
from configuration import Config 

app = create_app(config_class=Config)

@app.cli.command()
def init_db():
    """Create database tables"""
    with app.app_context():
        db.create_all()
    print('Database initialized.')

if __name__ == '__main__':
    app.run(debug=True)
