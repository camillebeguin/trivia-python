from config import CATEGORIES
from src.board import Board
from src.dice import Dice
from src.game import Game
from src.player import PlayerFactory
from src.question import QuestionManager


def play_trivia_game():
    board = Board(categories=CATEGORIES)
    game = Game()

    # enroll 3 players
    for name in ["John", "Jane", "Jack"]:
        player = PlayerFactory.create(categories=CATEGORIES, name=name)
        game.add_player(player)

    game.start_game()

    # game goes on until one player collected all the pie wedges
    while not game.is_over:
        game.current_player.move(board, Dice.roll())

        question = QuestionManager.generate_question(
            category=board.get_current_category(game.current_player.position)
        )

        is_correct_answer = game.current_player.answer_question(
            question, answer="madrid"
        )
        game.handle_answer(board, game.current_player, is_correct_answer)
