from fastapi import APIRouter, HTTPException
from typing import List
from schema import User, UserCreate
from user_store import UserStore

router = APIRouter()
store = UserStore("users.txt")


@router.get("/", response_model=List[User])
def get_users():
    return store.load()


@router.post("/", response_model=User)
def create_user(user: UserCreate):
    users = store.load()
    new_user = {
        "id": max([u["id"] for u in users], default=0) + 1,
        "name": user.name,
        "email": user.email
    }
    users.append(new_user)
    store.save(users)
    return new_user


@router.get("/search", response_model=List[User])
def search_users(q: str):
    users = store.load()
    return [u for u in users if q.lower() in u["name"].lower()]


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    user = store.find_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}")
def update_user(user_id: int, updated_user: UserCreate):
    success = store.update_user(
        user_id,
        {"name": updated_user.name, "email": updated_user.email}
    )
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated"}


@router.delete("/{user_id}")
def delete_user(user_id: int):
    success = store.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}