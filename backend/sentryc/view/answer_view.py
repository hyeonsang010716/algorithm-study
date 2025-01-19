from flask import Blueprint, request, jsonify
from model.geometry import p1027

ans_bp = Blueprint('answer', __name__)
@ans_bp.route('/chat/algorithm/', methods=['POST'])
def send_ans():
    input_list = request.json.get("input")
    
    answers = []
    
    for input in input_list:
        answer = p1027.solve(input)
        answers.append(str(answer))
        
    return jsonify({"answer": answers})

@ans_bp.route('/chat/problem_number/', methods=['POST'])
def send_num():
    return jsonify({"answer": 1027})