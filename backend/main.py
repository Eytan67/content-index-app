from fastapi import FastAPI

app = FastAPI()

@app.get("/creators")
async def get_creators():
    return [
        {"id": 1, "name": "Creator 1", "content": "Lesson about Python"},
        {"id": 2, "name": "Creator 2", "content": "Lesson about React"}
    ]