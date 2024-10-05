from uuid import uuid4

import pytest

from src.exceptions import GameRuleException, GameStateException
from src.game import Game, GameStatus
from src.player import Player
from tests.factories import PieFactory, PlayerFactory


def test_can_only_add_player_before_game_starts(categories):
    game = Game()

    # cannot start before adding players
    with pytest.raises(GameRuleException):
        game.start_game()

    # can add player before game starts
    assert game.status == GameStatus.init

    game.add_player(PlayerFactory.create(categories=categories))
    game.add_player(PlayerFactory.create(categories=categories))

    assert len(game.players) == 2

    game.start_game()
    assert game.status == GameStatus.processing

    # can no longer add players after game starts
    with pytest.raises(GameStateException):
        game.add_player(PlayerFactory.create(categories=categories))


def test_player_starts_with_no_wedges(categories):
    pie = PieFactory.create(categories=categories)
    player = Player(id=uuid4(), name="John", pie=pie)

    assert not player.has_won()
    assert not any(pie.pie)
