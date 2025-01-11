from flask import Flask
from view import answer_view

app = Flask(__name__)
app.register_blueprint(answer_view.ans_bp, url_prefix='/sentryc')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)