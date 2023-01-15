import unittest
from unittest.mock import patch, MagicMock

from fastapi.testclient import TestClient

from src.main import app
from src.exceptions.item_not_found_error import ItemNotFoundError


class TestReadItem(unittest.TestCase):
    def test_read_item(self):
        item_use_case_mock = MagicMock()
        item_use_case_mock.get_item.return_value = {"id": 1, "name": "item1", "description": "description1"}
        with patch("src.adapters.router.item_use_case", item_use_case_mock):
            client = TestClient(app)
            response = client.get("/items/1")
            assert response.status_code == 200
            assert response.json() == {"id": 1, "name": "item1", "description": "description1"}

    def test_read_item_not_found(self):
        item_use_case_mock = MagicMock()
        item_use_case_mock.get_item.side_effect = ItemNotFoundError("Item not found")
        with patch("src.adapters.router.item_use_case", item_use_case_mock):
            client = TestClient(app)
            response = client.get("/items/1")
            assert response.status_code == 404
            assert response.json() == {"detail": "Item not found"}

    def test_create_item(self):
        item_use_case_mock = MagicMock()
        item_use_case_mock.create_item.return_value = {"id": 1, "name": "item2", "description": "description2"}
        with patch("src.adapters.router.item_use_case", item_use_case_mock):
            client = TestClient(app)
            response = client.post("/items/", json={"name": "item2", "description": "description2"})
            assert response.status_code == 200
            assert response.json() == {"id": 1, "name": "item2", "description": "description2"}
