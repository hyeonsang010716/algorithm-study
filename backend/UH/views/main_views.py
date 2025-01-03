from flask import Blueprint, request
from models import p1167

bp = Blueprint('main', __name__, url_prefix='/UH')

@bp.route("/chat/algorithm/", methods=['GET'])
def get_hello():
    return "hello"

@bp.route("/chat/algorithm/", methods=['POST'])
def send_result():
    #TODO 백 프론트 연결은 성공 여기에 json을 받아서 어떻게 처리할 지 고민
    data = request.get_json()
    result = data["input"]
    return {"answer": "11"}