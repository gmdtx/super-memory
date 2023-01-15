from typing import Dict

from src.repositories.item_repository import ItemRepository, item_repository


class ItemUseCases:
    def __init__(self, repository: ItemRepository):
        self.repository = repository

    def get_item(self, item_id: int) -> Dict:
        return self.repository.get_item(item_id)

    def create_item(self, item: Dict) -> Dict:
        return self.repository.create_item(item)


item_use_case = ItemUseCases(item_repository)
