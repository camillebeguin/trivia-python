from enum import StrEnum

from src.board import Board
from src.exceptions import GameRuleException, GameStateException
from src.player import Player


class GameStatus(StrEnum):
    init = "init"
    processing = "processing"
    completed = "completed"


class Game:
    min_players: int = 2
    max_players: int = 6

    def __init__(self):
        self.players = []
        self.status = GameStatus.init
        self._current_player = 0

    @property
    def current_player(self) -> Player:
        return self.players[self._current_player]

    @property
    def is_over(self) -> bool:
        return self.status == GameStatus.completed

    @staticmethod
    def validate_players(n_players: int, min_players: int, max_players: int):
        if n_players < min_players:
            raise GameRuleException("not_enough_players")

        if n_players > max_players:
            raise GameRuleException("too_many_players")

    def start_game(self):
        self.validate_players(
            n_players=len(self.players),
            min_players=self.min_players,
            max_players=self.max_players,
        )

        self.status = GameStatus.processing

    def _end_game(self):
        self.status = GameStatus.completed

    def add_player(self, player):
        if self.status != GameStatus.init:
            raise GameStateException("game_already_started")

        self.players.append(player)

    def next_player(self):
        self._current_player = (self._current_player + 1) % len(self.players)

    def handle_answer(self, board: Board, player: Player, correct: bool):
        if correct:
            self.handle_correct_answer(board, player)
        else:
            self.handle_wrong_answer()

    def handle_correct_answer(self, board: Board, player: Player):
        player.get_pie_wedge(board)

        if player.has_won():
            self._end_game()

    def handle_wrong_answer(self):
        self.next_player()
