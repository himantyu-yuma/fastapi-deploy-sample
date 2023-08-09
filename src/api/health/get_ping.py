from fastapi import APIRouter

router = APIRouter()


@router.get("/ping")
def read_root():
    return {"Hello": "World"}
