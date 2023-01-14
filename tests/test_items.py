from unittest import mock

import pytest
from starlette.testclient import TestClient

from src.main import app
from src.repositories.item_repository import ItemRepository
from src.usecases.item_usecase import ItemUseCases


@pytest.fixture
def repository():
    repository = ItemRepository()
    repository.create_item({"name": "item1", "description": "description1"})
    repository.create_item({"name": "item2", "description": "description2"})
    return repository


def test_read_item(repository):
    with mock.patch.object(ItemUseCases, 'get_item') as mock_get_item:
        mock_get_item.return_value = {"id": 1, "name": "item1", "description": "description1"}
        service = ItemUseCases(repository)
        item = service.get_item(1)
        assert item == {"id": 1, "name": "item1", "description": "description1"}


def test_client_read_item():
    client = TestClient(app)
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "item1", "description": "description1"}


def test_read_item_not_found():
    client = TestClient(app)
    response = client.get("/items/10")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}


def test_client_create_item():
    client = TestClient(app)
    response = client.post("/items/", json={"name": "new_item", "description": "new_description"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "new_item", "description": "new_description"}
