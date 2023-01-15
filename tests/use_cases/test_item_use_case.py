import unittest
from unittest.mock import MagicMock

from src.repositories.item_repository import ItemRepository
from src.use_cases.item_use_case import ItemUseCases


class TestItemUseCases(unittest.TestCase):
    def setUp(self):
        self.repository = MagicMock(ItemRepository)
        self.use_cases = ItemUseCases(self.repository)
        self.item = {"name": "item1", "description": "description1"}

    def test_get_item(self):
        self.repository.get_item.return_value = self.item
        result = self.use_cases.get_item(1)
        self.repository.get_item.assert_called_with(1)
        assert result == self.item

    def test_create_item(self):
        self.repository.create_item.return_value = self.item
        result = self.use_cases.create_item(self.item)
        self.repository.create_item.assert_called_with(self.item)
        assert result == self.item
