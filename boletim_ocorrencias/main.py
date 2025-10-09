from fastapi import FastAPI
from routes import router

app = FastAPI()

app.include_router(router)

@app.get("/ping")
def pong():
    return {'message' : 'pong'}
