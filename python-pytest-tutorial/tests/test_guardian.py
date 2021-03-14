from typing import Tuple

from models.guardian import Guardian
import pytest


# @pytest.fixture
# def guardians() -> Tuple[Guardian, ...]:
#     g1 = Guardian('GFName1', 'GLName1')
#     g2 = Guardian('GFName2', 'GLName2')
#     g3 = Guardian('GFName3', 'GLName3')
#     return g1, g2, g3


def test_construction(guardians):
    # g = Guardian('GFName1', 'GLName1')
    assert "GFName1" == guardians[0].first_name
    assert "GLName1" == guardians[0].last_name
