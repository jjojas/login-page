from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from .db import SessionLocal, Base
from sqlalchemy.orm import Session
from sqlalchemy import Column, String
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class UserModel(BaseModel):
    username: str
    password: str

class User(Base):
    __tablename__ = 'users'
    username = Column(String, primary_key = True)
    password = Column(String, default = 'user')

def get_user_db(db: Session, username: str = None):
    if username is None:
        ret = {}
        for user in db.query(User).all():
            ret[user.username] = {}
            ret[user.username]["id"] = user.username
            ret[user.username]["password"] = user.password
        return ret
    else:
        return db.query(User).filter(User.username == username).first()

def add_user_db(db: Session, info: UserModel):
    User_model = User(**info.dict())
    db.add(User_model)
    db.commit()
    db.refresh(User_model)
    return User_model

def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"Hello" : "World"}

@app.get('/user/')
def get_user(db=Depends(db)):
    user = get_user_db(db,None)
    if user:
        return user
    else:
        raise HTTPException(404, detail= {"error" : "Can't get user"})

@app.get('/user/{username}')
def get_user(username: str, db=Depends(db)):
    user = get_user_db(db,username)
    if user:
        return user
    else:
        raise HTTPException(404, detail= {"error" : "Can't get user"})

@app.post('/user/')
def add_user(info: UserModel, db=Depends(db)):
    object_in_db = get_user_db(db, info.username)
    if object_in_db:
        raise HTTPException(400, detail= {"error" : "Can't add user"})
    return add_user_db(db,info)