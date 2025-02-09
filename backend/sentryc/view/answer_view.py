from flask import Blueprint, request, jsonify
import sqlite3

from model.string import p1013

ans_bp = Blueprint('answer', __name__)
@ans_bp.route('/chat/txt-algorithm/', methods=['POST'])
def send_ans():
    try:
        conn = sqlite3.connect("../../problems.db")
        
        cursur = conn.cursor()
        cursur.execute("SELECT * FROM algo")
        
        sql_input_list = cursur.fetchall()
    
        conn.close()
        
    except sqlite3.Error as e:
        print(f"Sqlite Error: {e}")
        
    answers = []
    
    input_list = sql_input_list[0][1].split("\n\n\n")
    for input in input_list:
        if input == "": continue
        answer = p1013.solve(input)
        answers.append(str(answer))
        
    return jsonify({"answer": answers})

@ans_bp.route('/chat/problem_number/', methods=['POST'])
def send_num():
    return jsonify({"answer": 1013})