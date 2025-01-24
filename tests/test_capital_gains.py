import requests

BASE_URL = "http://localhost:5003"

def test_capital_gains_endpoint():
    response = requests.get(f"{BASE_URL}/capital-gains")
    assert response.status_code == 200
    assert "total_gains" in response.json()

def test_capital_gains_with_filter():
    response = requests.get(f"{BASE_URL}/capital-gains?numsharesgt=5")
    assert response.status_code == 200
    assert "details" in response.json()
