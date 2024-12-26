from fastapi import FastAPI

import uvicorn
from api.router import api_router


def get_app() -> FastAPI:

    app = FastAPI()

    app.include_router(router=api_router, prefix="/hyeonsang")

    return app



if __name__ == "__main__":
    uvicorn.run(get_app(), host="0.0.0.0", port=8001)