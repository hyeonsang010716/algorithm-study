from fastapi import APIRouter
from fastapi import File, UploadFile
from api.util.formats import InRequest , OutResponse , OutProblemNumber
from model.instruction import p17430
import tempfile
import shutil
import os

router = APIRouter()

def save_upload_file(upload_file):
    with tempfile.NamedTemporaryFile(delete=False, dir="/tmp") as tmp_file:
        shutil.copyfileobj(upload_file.file, tmp_file)
        tmp_file_path = tmp_file.name

    # 임시 파일 경로 반환
    return tmp_file_path

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"{file_path} 파일이 삭제되었습니다.")
    else:
        print(f"{file_path} 파일이 존재하지 않습니다.")

@router.post("/txt-algorithm")
async def chat_with_openai(
    file: UploadFile = File(...)
) -> OutResponse:
    
    file_path = save_upload_file(file)

    with open(file_path, "r") as file:
        content = file.read() 
 
    try:
        
        answers = []

        for Input in content.split("\n\n\n\n"):
            print(Input)
            answer = p17430.solve(Input)

            answers.append(str(answer))

        return OutResponse(answer = answers)

    except Exception as e:
        return OutResponse(answer = [str(e)])
    
@router.post("/problem_number")
async def chat_with_openai() -> OutProblemNumber:

    return OutProblemNumber(answer = "17430")