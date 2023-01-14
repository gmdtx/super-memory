import unittest
from unittest.mock import patch

from src.entities.item import Item


class TestItem(unittest.TestCase):

    def test_create_item(self):
        with patch("src.entities.item.Item") as mocked_item:
            instance = mocked_item.return_value
            instance.name = "item1"
            instance.description = "description1"
            item = Item(name="item1", description="description1")
            assert item.name == "item1"
            assert item.description == "description1"
