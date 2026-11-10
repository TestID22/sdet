import pytest
import requests

@pytest.fixture
def base_url():
    return "http://localhost:3000"


@pytest.fixture
def api():
    session = requests.Session()
    yield session
    session.close()

