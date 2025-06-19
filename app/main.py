from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.database import db, init_db

app = FastAPI()

class Todo(BaseModel):
    title: str
    done: bool = False

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def home():
    return {"msg": "FastAPI deployed on AWS EKS with public URL!"}


@app.post("/todo")
def add_todo(todo: Todo):
    db.append(todo)
    return {"msg": "Added", "todo": todo}

@app.get("/todos")
def get_all():
    return db

@app.delete("/todo/{index}")
def delete_todo(index: int):
    try:
        db.pop(index)
        return {"msg": "Deleted"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Item not found")
