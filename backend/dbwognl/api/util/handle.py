from fastapi import APIRouter
from api.util.formats import InRequest , OutResponse
from model.dp import p1003

router = APIRouter()

@router.post("/algorithm/")
async def chat_with_openai(
    query: InRequest,
) -> OutResponse:

    try:
        answers = []

        for Input in query.input:
            
            answer = p1003.solve(Input) #####

            answers.append(str(answer))

        return OutResponse(answer = answers)

    except Exception as e:
        return OutResponse(answer = [str(e)])
