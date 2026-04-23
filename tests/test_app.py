import pytest
from src.api import app
from src.service import Service
from src.errors import NotFoundError


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


# --- API tests ---

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_get_item_not_found(client):
    response = client.get("/items/999")
    assert response.status_code == 404


# --- Service tests ---

def test_service_get_all_returns_list():
    svc = Service()
    result = svc.get_all()
    assert isinstance(result, list)


def test_service_get_by_id_raises_not_found():
    svc = Service()
    with pytest.raises(NotFoundError):
        svc.get_by_id(999)
