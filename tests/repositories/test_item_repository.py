import unittest

from src.repositories.item_repository import ItemRepository


class TestItemRepository(unittest.TestCase):
    def setUp(self):
        self.items = {1: {"id": 1, "name": "item1", "description": "description1"}}

    def test_get_item(self):
        repository = ItemRepository()
        repository.items = self.items
        item = repository.get_item(1)
        assert item == {"id": 1, "name": "item1", "description": "description1"}

    def test_create_item(self):
        repository = ItemRepository()
        item = {"name": "item1", "description": "description1"}
        created_item = repository.create_item(item)
        assert created_item == {"id": 1, "name": "item1", "description": "description1"}