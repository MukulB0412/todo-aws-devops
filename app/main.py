from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.database import todo_collection

app = FastAPI()

class Todo(BaseModel):
    title: str
    done: bool = False

@app.post("/todo")
def add_todo(todo: Todo):
    todo_collection.insert_one(todo.dict())
    return {"msg": "Added"}

@app.get("/todos")
def get_all():
    todos = list(todo_collection.find({}, {"_id": 0}))
    return todos

@app.delete("/todo/{title}")
def delete_todo(title: str):
    result = todo_collection.delete_one({"title": title})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Not found")
    return {"msg": "Deleted"}

