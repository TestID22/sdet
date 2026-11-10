import pytest
import requests


@pytest.mark.parametrize("category", ["electronics", "accessories", "furniture"])
def test_category_filter(base_url, category):
    response = requests.get(f"{base_url}/api/products", params={'category': category})
    assert response.status_code == 200,  "Products page is not available"
    products = response.json()
    assert len(products) > 0
    assert all(p["category"] == category for p in products)
    print("test")
    