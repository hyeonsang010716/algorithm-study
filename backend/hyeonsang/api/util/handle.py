from fastapi import APIRouter
from api.util.formats import InRequest , OutResponse , OutProblemNumber
from model.instruction import p17430

router = APIRouter()

@router.post("/algorithm")
async def chat_with_openai(
    query: InRequest,
) -> OutResponse:

    try:
        answers = []

        for Input in query.input:

            answer = p17430.solve(Input)

            answers.append(str(answer))

        return OutResponse(answer = answers)

    except Exception as e:
        return OutResponse(answer = [str(e)])
    
@router.post("/problem_number")
async def chat_with_openai() -> OutProblemNumber:

    return OutProblemNumber(answer = "17430")