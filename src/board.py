import random
from dataclasses import dataclass
from typing import List


class Board:
    n_boxes = 30
    random.seed(0)

    def __init__(self, categories: List[str]):
        self.categories = categories
        self.boxes = self._build_board(categories)

    def _build_board(self, categories) -> List[str]:
        """
        In the basic 30 boxes version, headquarters are located every 5 boxes,
        and categories are randomly distributed in other boxes, each category appearing 5 times in total
        """
        boxes = random.sample(
            categories * int(self.n_boxes / len(categories) - 1),
            self.n_boxes - len(categories),
        )

        for i in range(0, len(categories)):
            boxes.insert(i * 5, categories[i])

        return boxes

    def get_new_position(self, current_position: int, steps: int) -> int:
        return (current_position + steps) % self.n_boxes

    def get_current_category(self, position: int) -> str:
        return self.boxes[position]

    def is_headquarter(self, position: int) -> bool:
        return position % (self.n_boxes / len(self.categories)) == 0


@dataclass
class Pie:
    def __init__(self, categories: List[str]):
        self.categories = categories
        self.pie = [False for _ in categories]

    def add_wedge(self, category: str) -> None:
        self[category] = True

    def __setitem__(self, category: str, value: bool) -> None:
        category_index: int = self.categories.index(category)
        self.pie[category_index] = value

    def __bool__(self):
        return all(self.pie)
