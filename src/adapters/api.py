from fastapi import APIRouter, HTTPException, Depends

from src.entities.item import Item
from src.exceptions.item_not_found_error import ItemNotFoundError
from src.services.item_service import item_service
from src.usecases.item_usecase import ItemUseCases

router = APIRouter()


@router.get("/items/{item_id}")
async def read_item(item_id: int, service: ItemUseCases = Depends(item_service)):
    try:
        item = service.get_item(item_id)
        return item
    except ItemNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/items/")
async def create_item(item: Item, service: ItemUseCases = Depends(item_service)):
    new_item = service.create_item(item.dict())
    return new_item
