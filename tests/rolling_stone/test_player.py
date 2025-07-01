from geo_calculator.rolling_stone.player import Player


def test_player():
    player = Player()
    assert isinstance(player, Player)


def test_player_receive_score():
    # Arrange
    player = Player()
    RECEIVED_SCORE = 10
    assert player.score == 0
    # Act
    player.receive_score(RECEIVED_SCORE)
    # Assert
    assert player.score == RECEIVED_SCORE
