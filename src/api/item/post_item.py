from fastapi import APIRouter

from src.db.database import db

router = APIRouter()


@router.post("/api/items")
def update_items(req: str):
    return db.insert_one(req)