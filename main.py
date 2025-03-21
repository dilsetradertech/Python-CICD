from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

users_db = {}


class UserUpdate(BaseModel):
    name: str
    email: EmailStr


@app.post("/update-user/{user_id}")
def update_user(user_id: int, user: UserUpdate):
    users_db[user_id] = {"name": user.name, "email": user.email}
    return {"message": "User updated successfully", "user": users_db[user_id]}


@app.get("/get-user/{user_id}")
def get_user(user_id: int):
    user = users_db.get(user_id)
    if user:
        return {"user_id": user_id, "name": user["name"], "email": user["email"]}
    return {"error": "User not found"}


@app.get("/")
async def root():
    return {"message": "Hello World hello there"}
