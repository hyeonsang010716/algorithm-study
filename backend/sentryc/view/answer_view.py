from flask import Blueprint, request, jsonify
from model.greedy import p1041
import re

ans_bp = Blueprint('answer', __name__)
@ans_bp.route('/chat/txt-algorithm/', methods=['POST'])
def send_ans():
    input_file = request.files.get('file')
    input_list = re.split(r'\r?\n\r?\n\r?\n', input_file.read().decode('utf-8'))
    
    answers = []
    
    for input in input_list:
        if input == "": continue
        answer = p1041.solve(input)
        answers.append(str(answer))
        
    return jsonify({"answer": answers})

@ans_bp.route('/chat/problem_number/', methods=['POST'])
def send_num():
    return jsonify({"answer": 1041})