import unittest

from src.exceptions.item_not_found_error import ItemNotFoundError


class TestItemNotFoundError(unittest.TestCase):
    def test_item_not_found_error(self):
        with self.assertRaises(ItemNotFoundError):
            raise ItemNotFoundError
