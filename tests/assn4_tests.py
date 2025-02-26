import requests
import pytest

# Base URLs for the services
STOCKS_BASE_URL = "http://localhost:5001"
CAPITAL_GAINS_BASE_URL = "http://localhost:5003"

# ==============================
# Sample Stock Payloads
# ==============================
stock_alpha = {
    "name": "Tesla, Inc.",
    "symbol": "TSLA",
    "purchase_price": 650.00,
    "purchase_date": "2024-05-20",
    "shares": 12
}

stock_beta = {
    "name": "Microsoft Corporation",
    "symbol": "MSFT",
    "purchase_price": 210.50,
    "purchase_date": "2024-03-15",
    "shares": 15
}

stock_gamma = {
    "name": "Amazon.com, Inc.",
    "symbol": "AMZN",
    "purchase_price": 3200.99,
    "purchase_date": "2024-04-10",
    "shares": 5
}

# For testing missing required field "symbol"
stock_delta = {
    "name": "Meta Platforms, Inc.",
    "purchase_price": 280.50,
    "purchase_date": "2024-06-01",
    "shares": 8
}

# For testing invalid purchase date format
stock_epsilon = {
    "name": "Intel Corporation",
    "symbol": "INTC",
    "purchase_price": 54.75,
    "purchase_date": "06/01/2024",
    "shares": 20
}

@pytest.fixture(scope="module")
def test_data():
    """
    Fixture to store shared data between tests.
    """
    return {}

# ==============================
# Capital Gains Service Tests
# ==============================
def test_capital_gains_endpoint():
    response = requests.get(f"{CAPITAL_GAINS_BASE_URL}/capital-gains")
    assert response.status_code == 200
    assert "total_gains" in response.json(), "Missing 'total_gains' in response"

def test_capital_gains_with_filter():
    response = requests.get(f"{CAPITAL_GAINS_BASE_URL}/capital-gains?numsharesgt=5")
    assert response.status_code == 200
    assert "details" in response.json(), "Missing 'details' in response"

# ==============================
# Stocks Service Tests
# ==============================
def test_home():
    response = requests.get(f"{STOCKS_BASE_URL}/")
    assert response.status_code == 200
    assert "Welcome to the stocks" in response.text, "Unexpected homepage response"

def test_add_stocks():
    stocks = [stock_alpha, stock_beta, stock_gamma]
    ids = set()
    for stock in stocks:
        response = requests.post(f"{STOCKS_BASE_URL}/stocks", json=stock)
        assert response.status_code == 201, f"Failed to add stock: {stock['symbol']}"
        assert "id" in response.json(), "Response does not contain 'id'"
        ids.add(response.json()["id"])
    assert len(ids) == 3, "IDs are not unique"

def test_get_stock_by_id():
    response = requests.get(f"{STOCKS_BASE_URL}/stocks")
    assert response.status_code == 200
    stocks = response.json()
    assert stocks, "Stock list is empty"
    stock_id = stocks[0]["id"]

    response = requests.get(f"{STOCKS_BASE_URL}/stocks/{stock_id}")
    assert response.status_code == 200
    assert "symbol" in response.json(), "Response missing 'symbol'"

def test_get_all_stocks():
    response = requests.get(f"{STOCKS_BASE_URL}/stocks")
    assert response.status_code == 200
    assert len(response.json()) >= 3, "Expected at least 3 stocks, found different amount"

def test_get_stock_values():
    response = requests.get(f"{STOCKS_BASE_URL}/stocks")
    assert response.status_code == 200
    stocks = response.json()
    for stock in stocks:
        resp = requests.get(f"{STOCKS_BASE_URL}/stock-value/{stock['id']}")
        assert resp.status_code == 200
        assert "symbol" in resp.json(), "Response missing 'symbol'"

def test_get_portfolio_value():
    response = requests.get(f"{STOCKS_BASE_URL}/portfolio-value")
    assert response.status_code == 200
    assert "portfolio_value" in response.json(), "Missing 'portfolio_value' in response"

def test_add_stock_missing_symbol():
    response = requests.post(f"{STOCKS_BASE_URL}/stocks", json=stock_delta)
    assert response.status_code == 400, "Adding stock without symbol should fail"

def test_add_stock_invalid_date():
    response = requests.post(f"{STOCKS_BASE_URL}/stocks", json=stock_epsilon)
    assert response.status_code == 400, "Adding stock with invalid date should fail"

def test_delete_stock():
    response = requests.get(f"{STOCKS_BASE_URL}/stocks?symbol=MSFT")
    stocks = response.json()
    if stocks:
        stock_id = stocks[0]['id']
        delete_response = requests.delete(f"{STOCKS_BASE_URL}/stocks/{stock_id}")
        assert delete_response.status_code == 204, "Unexpected status code on delete"

        response = requests.get(f"{STOCKS_BASE_URL}/stocks/{stock_id}")
        assert response.status_code == 404, "Deleted stock should not exist anymore"
    else:
        pytest.skip("No stock found to delete")
