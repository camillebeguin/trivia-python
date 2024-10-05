import pytest

from config import CATEGORIES
from src.board import Board
from src.game import Game
from src.player import Player
from tests.factories import PlayerFactory


@pytest.fixture
def categories() -> list[str]:
    return CATEGORIES


@pytest.fixture
def board(categories) -> Board:
    return Board(categories=categories)


@pytest.fixture
def players(categories, n: int = 3) -> list[Player]:
    return [PlayerFactory.create(categories=categories) for _ in range(n)]


@pytest.fixture
def game(players) -> Game:
    game = Game()

    for player in players:
        game.add_player(player)

    game.start_game()
    return game
