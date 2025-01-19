from flask import Blueprint, request
from models.main import get_answer

bp = Blueprint('main', __name__, url_prefix='/UH')

pro_num = 25379

@bp.route("/chat/algorithm", methods=['POST'])
def send_result():
    input_data = request.get_json()["input"]
    return get_answer(pro_num, input_data)

@bp.route("/chat/problem_number", methods=["POST"])
def send_problem_number():
    return {"answer": pro_num}