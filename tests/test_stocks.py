import requests

BASE_URL = "http://localhost:5001"

def test_home():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert "Welcome to the stocks1" in response.text

def test_add_stock():
    data = {
        "symbol": "AAPL",
        "name": "Apple Inc.",
        "purchase price": 150.5,
        "purchase date": "2024-01-01",
        "shares": 10
    }
    response = requests.post(f"{BASE_URL}/stocks", json=data)
    assert response.status_code == 201
    assert "id" in response.json()

def test_get_stock():
    response = requests.get(f"{BASE_URL}/stocks?symbol=AAPL")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_delete_stock():
    response = requests.get(f"{BASE_URL}/stocks?symbol=AAPL")
    stock_id = response.json()[0]['id']
    delete_response = requests.delete(f"{BASE_URL}/stocks/{stock_id}")
    assert delete_response.status_code == 204
