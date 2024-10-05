from uuid import UUID

from faker import Faker

from src.board import Board, Pie
from src.question import Question

faker = Faker(locale="fr_FR")


class Player:
    def __init__(self, id: UUID, name: str, pie: Pie):
        self.id = id
        self.name = name
        self.pie = pie
        self.position = 0

    def has_won(self) -> bool:
        return bool(self.pie)

    def move(self, board: Board, steps: int):
        self.position = board.get_new_position(self.position, steps)

    def answer_question(self, question: Question, answer: str) -> bool:
        return question.check_answer(answer)

    def get_pie_wedge(self, board: Board):
        if board.is_headquarter(self.position):
            category = board.get_current_category(self.position)
            self.pie.add_wedge(category=category)
