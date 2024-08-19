from iris import load_data
import sys
import os
import pytest

# Add the directory where 'iris.py' is located to sys.path
sys.path.insert(0, '/mnt/d/GitHub/CICD')

# Import the module we want to test


@pytest.fixture
def iris_data():
    """Fixture to load the Iris data."""
    return load_data()
