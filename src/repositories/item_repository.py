from typing import Dict

from src.exceptions.item_not_found_error import ItemNotFoundError


class ItemRepository:
    def __init__(self):
        self.items = {}
        self.last_id = 0

    def get_item(self, item_id: int) -> Dict:
        item = self.items.get(item_id)
        if not item:
            raise ItemNotFoundError("Item not found")
        return item

    def create_item(self, item: Dict) -> Dict:
        self.last_id += 1
        item['id'] = self.last_id
        self.items[self.last_id] = item
        return item
