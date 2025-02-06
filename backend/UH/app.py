from flask import Flask
from models import db
from dotenv import load_dotenv
import os


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///' + os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")) + '/problems.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from views import main_views
    app.register_blueprint(main_views.bp)
    
    return app

if __name__ == "__main__":
    load_dotenv()
    app = create_app()
    app.run(host='localhost', port=8001)