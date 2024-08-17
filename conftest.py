from iris import load_data
from iris import load_data  # Now this should work
import sys
import os
import pytest

# Add the parent directory (CICD) to sys.path
# This is necessary to import the module we want to test
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..')))
# Now we can import the module we want to test


@pytest.fixture
def iris_data():
    """Fixture to load the Iris data."""
    return load_data()
