from typing import Dict

from src.repositories.item_repository import ItemRepository


class ItemUseCases:
    def __init__(self, repository: ItemRepository):
        self.repository = repository

    def get_item(self, item_id: int) -> Dict:
        return self.repository.get_item(item_id)

    def create_item(self, item: Dict) -> Dict:
        return self.repository.create_item(item)
