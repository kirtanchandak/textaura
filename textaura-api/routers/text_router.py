from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_pre_curated_lists():
    return {"HEllo"}

@router.get("/chandak")
def get_pre_curated_lists():
    return {"I am from chandak!"}