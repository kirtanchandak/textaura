from fastapi import APIRouter
from functions.generate_text import generate_from_youtube
router = APIRouter()
from pydantic import BaseModel


class QueryData(BaseModel):
    video_id: str


@router.get("/get_content")
def get_pre_curated_lists(query_data: QueryData):
    result = generate_from_youtube(video_id=query_data.video_id)
    return result

@router.get("/get")
def get_pre_curated_lists(video_id: str):
    result = generate_from_youtube(video_id=video_id)
    return result

@router.get("/chandak")
def get_pre_curated_lists():
    return {"I am from chandak!"}