from iris import load_data  # Now this should work
import sys
import os
import pytest

# Add the parent directory (CICD) to sys.path
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..')))


@pytest.fixture
def iris_data():
    """Fixture to load the Iris data."""
    return load_data()
