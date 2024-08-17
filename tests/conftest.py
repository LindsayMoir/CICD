# tests/conftest.py
import pytest
from iris import load_data 

@pytest.fixture
def iris_data():
    """Fixture to load the Iris data."""
    return load_data()
