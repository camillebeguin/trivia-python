class Question:
    def __init__(self, title: str, answer: str):
        self.title = title
        self.answer = answer

    def check_answer(self, answer: str) -> bool:
        return self.answer == answer.lower()


class QuestionManager:
    @staticmethod
    def generate_question(category: str) -> Question:
        # TODO: fetch questions from database or API
        return Question(title=f"What is the capital of Spain?", answer="madrid")
