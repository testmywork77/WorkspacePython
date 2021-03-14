from models.player import Player
from models.guardian import Guardian
from typing import Tuple
import pytest


# @pytest.fixture
# def player_one() -> Player:
#     return Player('PFName1', 'PLName1')
#
#
# @pytest.fixture
# def guardians() -> Tuple[Guardian, ...]:
#     g1 = Guardian('GFName1', 'GLName1')
#     g2 = Guardian('GFName2', 'GLName2')
#     g3 = Guardian('GFName3', 'GLName3')
#     return g1, g2, g3


def test_construction(player_one):
    assert 'PFName1' == player_one.first_name
    assert 'PLName1' == player_one.last_name
    assert [] == player_one.guardians


def test_add_guardian(player_one, guardians):
    player_one.add_guardian(guardians[0])
    assert [guardians[0]] == player_one.guardians


def test_add_guardians(player_one, guardians):
    # Add one guardian
    player_one.add_guardian(guardians[0])

    # Add second and third guardian
    # p.add_guardians([g2, g3])  # pass as List
    player_one.add_guardians((guardians[1], guardians[2]))  # pass as Tuple
    assert list(guardians) == player_one.guardians


def test_primary_guardian(player_one, guardians):
    # Add one guardian
    player_one.add_guardian(guardians[0])
    # g2 = Guardian('GFName2', 'GLName2')
    # g3 = Guardian('GFName3', 'GLName3')

    # player_one.add_guardians([g2, g3])
    player_one.add_guardians((guardians[1], guardians[2]))
    assert guardians[0] == player_one.primary_guardian

