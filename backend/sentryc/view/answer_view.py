from flask import Blueprint, request, jsonify
from model.math import p1010

ans_bp = Blueprint('answer', __name__)
@ans_bp.route('/chat/algorithm/', methods=['POST'])
def send_ans():
    input_list = request.json.get("input")
    
    answers = []
    
    for input in input_list:
        answer = p1010.solve(input)
        answers.append(str(answer))
        
    return jsonify({"answer": answers})