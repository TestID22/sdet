import requests
import pytest 


def test_products_edpoint_is_up(base_url):
    response = requests.get(f"{base_url}/api/products")
    assert response.status_code == 200

    products = response.json()
    assert isinstance(products, list)
    assert len(products) > 0


def test_has_products(base_url, all_products):
    assert len(all_products) > 0