from flask import Flask
from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)

    from views import main_views
    app.register_blueprint(main_views.bp)
    
    return app

if __name__ == "__main__":
    load_dotenv()
    app = create_app()
    app.run(host='localhost', port=8001)