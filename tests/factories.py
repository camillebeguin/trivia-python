from typing import List
from uuid import uuid4

from faker import Faker

from src.board import Pie
from src.player import Player

faker = Faker(locale="fr_FR")


class PieFactory:
    @staticmethod
    def create(categories: List[str]) -> Pie:
        return Pie(categories)


class PlayerFactory:
    @staticmethod
    def create(categories: list[str], **kwargs) -> Player:
        pie = PieFactory.create(categories=categories)
        return Player(
            **{
                "id": uuid4(),
                "name": faker.first_name(),
                "pie": pie,
                **kwargs,
            }
        )
