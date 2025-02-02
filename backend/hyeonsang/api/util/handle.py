from fastapi import APIRouter
from fastapi import File, UploadFile
from api.util.formats import InRequest , OutResponse , OutProblemNumber
from model.instruction import p17430
import tempfile
import shutil
import sqlite3
import os

router = APIRouter()

@router.post("/txt-algorithm")
async def chat_with_openai() -> OutResponse:
 
    try:
        conn = sqlite3.connect("../../problems.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM algo")
        answers = []
        rows = cursor.fetchall()
        content =""
        for row in rows:
            content = row[1]            

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