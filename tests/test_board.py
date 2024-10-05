from collections import Counter

import pytest

from tests.factories import PlayerFactory


def test_categories_are_evenly_distributed_on_board(board):
    assert len(board.boxes) == board.n_boxes, f"Board should have 30 boxes"

    assert [
        board.get_current_category(i) for i in [0, 5, 10, 15, 20, 25]
    ] == board.categories, f"Headquarters should be ordered and appear every 5 steps"

    category_counts = Counter(board.boxes)
    assert all(nb_occurrences == 5 for nb_occurrences in category_counts.values())


def test_move_player_on_board_updates_position(board):
    player = PlayerFactory.create(categories=board.categories)

    assert player.position == 0

    player.move(board, 5)
    assert player.position == 5

    player.move(board, 5)
    assert player.position == 10

    player.move(board, 20)
    assert player.position == 0


def test_player_can_move_around_board(game, board):
    for _ in range(30):
        game.current_player.move(board, 1)

    # after 30 moves, player should be back at the initial position
    assert game.current_player.position == 0

    game.current_player.move(board, 5)
    assert game.current_player.position == 5
