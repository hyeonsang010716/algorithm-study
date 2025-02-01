from fastapi import APIRouter
from api.util.formats import InRequest , OutResponse
from model.data_structures import p10773

router = APIRouter()

@router.post("/algorithm")
async def chat_with_openai(
    query: InRequest,
) -> OutResponse:

    try:
        answers = []
        
        for Input in query.input:
            
            answer = p10773.solve(Input) #####

            answers.append(str(answer))

        return OutResponse(answer = answers)

    except Exception as e:
        return OutResponse(answer = [str(e)])
