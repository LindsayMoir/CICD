import sys
import os
import pytest

# Add the parent directory (CICD) to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Now we can import the module we want to test
from iris import load_data

@pytest.fixture
def iris_data():
    """Fixture to load the Iris data."""
    return load_data()