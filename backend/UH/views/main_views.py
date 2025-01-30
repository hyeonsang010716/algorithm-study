from flask import Blueprint, request
from models.main import get_answer
import os


bp = Blueprint('main', __name__, url_prefix='/UH')

upload_folder = "./upload"
pro_num = 1918

@bp.route("/chat/txt-algorithm", methods=['POST'])
def send_result():
    file = request.files['file']
    
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    
    file_path = os.path.join("./upload", "tmp.txt")
    file.save(file_path)

    print(file_path)

    os.remove(file_path)
    return {'answer': '1'}, 200

@bp.route("/chat/problem_number", methods=["POST"])
def send_problem_number():
    return {"answer": pro_num}