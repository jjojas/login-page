from fastapi import FastAPI, Depends, HTTPException
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

users = { "admin" : { "id" : "admin", "password" : "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92" }, "admin2" : { "id" : "admin2", "password" : "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92" }}
class UserModel(BaseModel):
    username: str
    password: str


@app.get("/")
async def root():
    return {"Hello" : "World"}

@app.get('/user/')
def get_users():
    if users:
        return users
    else:
        raise HTTPException(404, detail= {"error" : "Can't get user"})
    
@app.get('/user/{username}')
def get_user(username: str):
    user = users[username]
    if user:
        return user
    else:
        raise HTTPException(404, detail= {"error" : "Can't get user"})