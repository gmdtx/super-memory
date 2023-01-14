from src.repository.item_repository import ItemRepository
from src.usecase.item_usecase import ItemUseCases


def item_service() -> ItemUseCases:
    repository = ItemRepository()
    return ItemUseCases(repository)
