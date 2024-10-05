import pytest

from src.question import QuestionManager


def test_player_only_collects_wedge_for_correct_answer_on_headquarter(
    game,
    board,
):
    # initial position is a headquarter position
    assert game.current_player.position == 0
    assert board.is_headquarter(game.current_player.position)

    current_category = board.get_current_category(game.current_player.position)
    question = QuestionManager.generate_question(category=current_category)

    is_correct_answer = game.current_player.answer_question(
        question, answer=question.answer
    )
    assert is_correct_answer

    game.handle_answer(board, game.current_player, is_correct_answer)
    assert game.current_player.pie.pie[0]
    assert sum(game.current_player.pie.pie) == 1

    # move to next box, not a headquarter so no wedge should be collected
    game.current_player.move(board, 1)
    assert not board.is_headquarter(game.current_player.position)

    current_category = board.get_current_category(game.current_player.position)
    question = QuestionManager.generate_question(category=current_category)

    game.handle_answer(board, game.current_player, correct=True)

    assert sum(game.current_player.pie.pie) == 1


def test_player_does_not_collect_wedge_for_incorrect_answer_and_turn_ends(game, board):
    # save a reference to the initial player
    initial_player = game.current_player

    # initial position is a headquarter position
    assert game.current_player.position == 0
    assert board.is_headquarter(game.current_player.position)

    current_category = board.get_current_category(game.current_player.position)
    question = QuestionManager.generate_question(category=current_category)

    is_correct_answer = game.current_player.answer_question(
        question, answer="wrong answer"
    )
    assert is_correct_answer == False

    game.handle_answer(board, game.current_player, is_correct_answer)

    # player should not have collected a wedge, and the game moves to the next player
    assert not any(initial_player.pie.pie)
    assert game.current_player != initial_player


def test_player_wins_game_after_correct_final_question(game, board):
    # current player has a pie with all wedges except one
    for _ in range(5):
        game.current_player.move(board, 5)
        game.current_player.get_pie_wedge(board)

    assert sum(game.current_player.pie.pie) == 5
    assert not game.is_over

    # move to the last headquarter, 6th category
    game.current_player.move(board, 5)

    current_category = board.get_current_category(game.current_player.position)
    question = QuestionManager.generate_question(category=current_category)

    is_correct_answer = game.current_player.answer_question(
        question, answer=question.answer
    )
    game.handle_answer(board, game.current_player, is_correct_answer)

    assert game.current_player.has_won()
    assert all(game.current_player.pie.pie)
    assert game.is_over
