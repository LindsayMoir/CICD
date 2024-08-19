import os
import sys
import pytest

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..')))

# Import the module we want to test
from iris import load_data

@pytest.fixture
def iris_data():
    """Fixture to load the Iris data."""
    return load_data()
