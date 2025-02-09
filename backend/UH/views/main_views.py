from flask import Blueprint, request, jsonify
from problems.main import get_answer
from models import db
from models.problems import algo
import os


bp = Blueprint('main', __name__, url_prefix='/UH')

upload_folder = "./upload"
pro_num = 1436

@bp.route("/chat/txt-algorithm", methods=['POST'])
def send_result():
    data = []
    with db.session.begin():
        inputs = db.session.query(algo.problem).all()
        for i in inputs:
            data.append(i[0].split('\n\n\n'))
    result = get_answer(pro_num, data[0][:-1])

    return jsonify(result), 200

@bp.route("/chat/problem_number", methods=["POST"])
def send_problem_number():
    return {"answer": pro_num}