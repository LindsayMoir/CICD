import sys
import pytest

# Add the directory where 'iris.py' is located to sys.path
sys.path.insert(0, '/mnt/d/GitHub/CICD') 

# Import the module we want to test
from iris import load_data

@pytest.fixture
def iris_data():
    """Fixture to load the Iris data."""
    return load_data()
