from datetime import date

import pytest
from src.api import app
from src.service import Service


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


def test_check_availability_incorrect_date_format(client):
    response = client.get("/apartments/1/availability?start_date=18-03-2024&end_date=25-03-2024")
    assert response.status_code == 400


# --- Service tests ---

def test_service_check_apartment_availability_returns_tuple():
    svc = Service()
    result = svc.check_apartment_availability(1, date(2024, 3, 19), date(2024, 3, 25))
    assert isinstance(result, tuple)
