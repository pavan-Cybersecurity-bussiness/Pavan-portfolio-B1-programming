from fastapi import APIRouter, HTTPException
from typing import List
from schema import User, UserCreate
from user_store import UserStore

router = APIRouter()
store = UserStore("users.db")


@router.get("/", response_model=List[User])
def get_users():
    return store.load()


@router.post("/", response_model=User)
def create_user(user: UserCreate):
    return store.save(user.dict())


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    user = store.find_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}")
def update_user(user_id: int, updated_user: UserCreate):
    success = store.update_user(user_id, updated_user.dict())

    if not success:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User updated successfully"}


@router.delete("/{user_id}")
def delete_user(user_id: int):
    success = store.delete_user(user_id)

    if not success:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User deleted successfully"}