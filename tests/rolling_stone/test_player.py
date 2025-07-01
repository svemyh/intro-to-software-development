import pytest
from geo_calculator.rolling_stone.player import Player


@pytest.fixture
def new_player():
    return Player()


def test_player(new_player):
    assert isinstance(new_player, Player)


def test_player_receive_score(new_player):
    # Arrange
    RECEIVED_SCORE = 10
    assert new_player.score == 0
    # Act
    new_player.receive_score(RECEIVED_SCORE)
    # Assert
    assert new_player.score == RECEIVED_SCORE
