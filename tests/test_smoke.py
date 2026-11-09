import requests
import pytest 


BASE_URL = "http://localhost:3000"


def test_products_edpoint_is_up():
    response = requests.get(f"{BASE_URL}/api/products")
    assert response.status_code == 200

    products = response.json()
    assert isinstance(products, list)
    assert len(products) > 0
