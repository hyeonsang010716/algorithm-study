from flask import Blueprint, request
from models import p1167

bp = Blueprint('main', __name__, url_prefix='/UH')

@bp.route("/chat/algorithm/", methods=['GET'])
def get_hello():
    return "hello"

@bp.route("/chat/algorithm/", methods=['POST'])
def send_result():
    data = request.get_json()
    input = data["input"]
    result = p1167.get_answer(input)
    return {"answer": str(result)}