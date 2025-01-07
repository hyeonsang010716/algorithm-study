from flask import Blueprint, request
from models import get_answer

bp = Blueprint('main', __name__, url_prefix='/UH')

@bp.route("/chat/algorithm/", methods=['GET'])
def get_hello():
    return "hello"

@bp.route("/chat/algorithm/", methods=['POST'])
def send_result():
    pro_num = 1967
    input = request.get_json()["input"]
    return {"answer": [str(get_answer(pro_num, input))], "tag": "dp"}
