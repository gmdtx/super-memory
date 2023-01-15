from fastapi import APIRouter, HTTPException

from src.entities.item import Item
from src.exceptions.item_not_found_error import ItemNotFoundError
from src.use_cases.item_use_case import item_use_case

api_router = APIRouter()


@api_router.get("/items/{item_id}")
def read_item(item_id: int):
    try:
        item = item_use_case.get_item(item_id)
    except ItemNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return item


@api_router.post("/items/")
def create_item(item: Item):
    new_item = item_use_case.create_item(item.dict())
    return new_item
