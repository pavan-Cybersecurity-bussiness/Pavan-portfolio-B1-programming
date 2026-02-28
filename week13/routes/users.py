from fastapi import APIRouter, HTTPException
from schema import User, UserCreate
import json
import os
from typing import List

router = APIRouter()

FILE_PATH = "users.txt"


# ----------------------
# Helper Functions
# ----------------------

def read_users():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as file:
        try:
            return json.load(file)
        except:
            return []


def write_users(users):
    with open(FILE_PATH, "w") as file:
        json.dump(users, file, indent=4)


def get_next_id(users):
    if not users:
        return 1
    return max(user["id"] for user in users) + 1


# ----------------------
# Routes
# ----------------------

@router.post("/", response_model=User)
def create_user(user: UserCreate):
    users = read_users()
    new_user = {
        "id": get_next_id(users),
        "name": user.name,
        "email": user.email
    }
    users.append(new_user)
    write_users(users)
    return new_user


@router.get("/", response_model=List[User])
def get_users():
    return read_users()


# IMPORTANT: search BEFORE {id}
@router.get("/search", response_model=List[User])
def search_users(q: str):
    users = read_users()
    return [user for user in users if q.lower() in user["name"].lower()]


@router.get("/{id}", response_model=User)
def get_user(id: int):
    users = read_users()
    for user in users:
        if user["id"] == id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@router.put("/{id}", response_model=User)
def update_user(id: int, updated_user: UserCreate):
    users = read_users()
    for user in users:
        if user["id"] == id:
            user["name"] = updated_user.name
            user["email"] = updated_user.email
            write_users(users)
            return user
    raise HTTPException(status_code=404, detail="User not found")


@router.delete("/{id}")
def delete_user(id: int):
    users = read_users()
    for user in users:
        if user["id"] == id:
            users.remove(user)
            write_users(users)
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")