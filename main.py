from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/todos")
def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = crud.get_todos(db, skip, limit)
    return todos


@app.post("/todos")
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    db_todo = crud.create_todo(db, todo)
    return db_todo


@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, done: bool, db: Session = Depends(get_db)):
    db_todo = crud.update_todo(db, todo_id, done)
    return db_todo
