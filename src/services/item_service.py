from src.repositories.item_repository import ItemRepository
from src.usecases.item_usecase import ItemUseCases


def item_service() -> ItemUseCases:
    repository = ItemRepository()
    return ItemUseCases(repository)
