# ----------------------------------------------
# fixture(s) shared across all the test modules
# ----------------------------------------------

# Imports
import pytest
from stuff.accum import Accumulator

@pytest.fixture
def accum():
    return Accumulator()
