from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="User registration")
list_user = []

# Creation model
class User(BaseModel):
    id: int
    name: str
    age: int
    cpf: str
    email: str

# Display model
class UserOut(BaseModel):
    id: int
    name: str
    email: str

# View all users
@app.get("/User")
async def view_user():
    return list_user

# Add User
@app.post("/User", response_model=UserOut, status_code=201)
async def new_user(user: User):
    user.id = len(list_user) + 1
    list_user.append(user)
    return user

# View by id
@app.get("/User/{id}", response_model=UserOut)
async def user_by_id(id: int):
    index = id - 1
    if index < 0 or index >= len(list_user):
        raise HTTPException(status_code=404, detail="User not found")
    return list_user[index]

# Update user
@app.put("/User/{id}", response_model=UserOut)
async def update_user(id: int, user: User):
    index = id - 1
    if index < 0 or index >= len(list_user):
        raise HTTPException(status_code=404, detail="User not found")

    user.id = id
    list_user[index] = user
    return user

# Delete user
@app.delete("/User/{id}")
async def delete_user(id: int):
    index = id - 1
    if index < 0 or index >= len(list_user):
        raise HTTPException(status_code=404, detail="User not found")

    deleted = list_user.pop(index)
    return {"message": "User successfully deleted", "deleted": deleted}
