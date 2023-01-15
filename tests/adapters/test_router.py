import unittest
from unittest import mock

from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient

from src.exceptions.item_not_found_error import ItemNotFoundError
from src.main import app


@patch("src.use_cases.item_use_case.ItemUseCases")
def test_read_item(item_use_cases_mock):
    # Create a mock for the ItemUseCases class
    item_use_cases = mock.Mock()
    # Define the return value for the get_item method
    item_use_cases.get_item.return_value = {"id": 1, "name": "item1", "description": "description1"}
    item_use_cases_mock.return_value = item_use_cases
    client = TestClient(app)
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "item1", "description": "description1"}


class TestReadItem(unittest.TestCase):
    @patch("src.adapters.router.use_case")
    def test_read_item_success(self, use_case_mock):
        # Create a mock for the ItemUseCases class
        use_case = MagicMock()
        # Define the return value for the get_item method
        use_case.get_item.return_value = {"id": 1, "name": "item1", "description": "description1"}

        client = TestClient(app)
        response = client.get("/items/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"id": 1, "name": "item1", "description": "description1"})

    @patch("src.adapters.router.use_case")
    def test_read_item_not_found(self, use_case_mock):
        # Create a mock for the ItemUseCases class
        use_case = MagicMock()
        # Define the side effect for the get_item method
        use_case.get_item.side_effect = ItemNotFoundError("Item not found")

        client = TestClient(app)
        response = client.get("/items/1")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"detail": "Item not found"})

# @patch("src.services.item_service.item_service")
# def test_create_item(item_service_mock):
#     service = mock.Mock()
#     service.create_item.return_value = {"id": 1, "name": "item2", "description": "description2"}
#     item_service_mock.return_value = service
#     client = TestClient(app)
#     response = client.post("/items/", json={"name": "item2", "description": "description2"})
#     assert response.status_code == 200
#     assert response.json() == {"id": 1, "name": "item2", "description": "description2"}
