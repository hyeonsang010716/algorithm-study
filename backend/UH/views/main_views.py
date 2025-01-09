from flask import Blueprint, request
from models.main import get_answer

bp = Blueprint('main', __name__, url_prefix='/UH')


@bp.route("/chat/algorithm/", methods=['POST'])
def send_result():
    pro_num = 25344
    input_data = request.get_json()["input"]
    return get_answer(pro_num, input_data)
