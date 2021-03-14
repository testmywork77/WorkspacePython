from models.player import Player
from models.guardian import Guardian
from typing import Tuple
import pytest


@pytest.fixture
def player_one() -> Player:
    return Player('PFName1', 'PLName1')


@pytest.fixture
def guardians() -> Tuple[Guardian, ...]:
    g1 = Guardian('GFName1', 'GLName1')
    g2 = Guardian('GFName2', 'GLName2')
    g3 = Guardian('GFName3', 'GLName3')
    return g1, g2, g3


@pytest.fixture
def guardians() -> Tuple[Guardian, ...]:
    g1 = Guardian('GFName1', 'GLName1')
    g2 = Guardian('GFName2', 'GLName2')
    g3 = Guardian('GFName3', 'GLName3')
    return g1, g2, g3