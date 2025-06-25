from fastapi import FastAPI
from app.routers.user.user import router as router_user

app = FastAPI()

app.include_router(router_user)


@app.get("/")
async def root():
        return {"message": "Hello Bigger Applications!"}