from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello_w():
    return {"Hello": "World"}