import requests

# ==============================
# Capital Gains Service Tests
# ==============================
CAPITAL_GAINS_BASE_URL = "http://localhost:5003"

def test_capital_gains_endpoint():
    response = requests.get(f"{CAPITAL_GAINS_BASE_URL}/capital-gains")
    assert response.status_code == 200
    assert "total_gains" in response.json()

def test_capital_gains_with_filter():
    response = requests.get(f"{CAPITAL_GAINS_BASE_URL}/capital-gains?numsharesgt=5")
    assert response.status_code == 200
    assert "details" in response.json()

# ==============================
# Stocks Service Tests
# ==============================
STOCKS_BASE_URL = "http://localhost:5001"

def test_home():
    response = requests.get(f"{STOCKS_BASE_URL}/")
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
    response = requests.post(f"{STOCKS_BASE_URL}/stocks", json=data)
    assert response.status_code == 201
    assert "id" in response.json()

def test_get_stock():
    response = requests.get(f"{STOCKS_BASE_URL}/stocks?symbol=AAPL")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_delete_stock():
    response = requests.get(f"{STOCKS_BASE_URL}/stocks?symbol=AAPL")
    stock_id = response.json()[0]['id']
    delete_response = requests.delete(f"{STOCKS_BASE_URL}/stocks/{stock_id}")
    assert delete_response.status_code == 204
