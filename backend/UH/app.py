from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///' + os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")) + '/problems.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    print('INFO: ', app.config['SQLALCHEMY_DATABASE_URI'])

    db.init_app(app)

    from views import main_views
    app.register_blueprint(main_views.bp)
    
    return app

if __name__ == "__main__":
    load_dotenv()
    app = create_app()
    app.run(host='localhost', port=8001)