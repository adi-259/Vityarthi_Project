import random
from questions import QUESTIONS
from scoring import score_answer
from algorithms import count_correct

class Quiz:
    def __init__(self, question_count=10):
        if not 1 <= question_count <= len(QUESTIONS):
            raise ValueError(f"question_count must be between 1 and {len(QUESTIONS)}")
        self.question_count = question_count
        # random.sample guarantees no repeated question in one attempt.
        self.questions = random.sample(QUESTIONS, self.question_count)
        self.answers = []

    def run(self):
        print("CSE1021 Quiz Platform")
        print(f"Random quiz: {self.question_count} questions selected from {len(QUESTIONS)}")
        score = 0

        for number, (question, options, answer_key) in enumerate(self.questions, start=1):
            print(f"\nQuestion {number}: {question}")
            for i, option in enumerate(options):
                print(f"{chr(65+i)}. {option}")

            answer = input("Answer: ").strip().upper()
            correct = answer == answer_key
            self.answers.append(correct)

            if correct:
                print("Correct!")
                score += score_answer(True)
            else:
                print("Incorrect. Correct answer:", answer_key)

        print("\nFinal score:", score)
        print("Correct answers:", count_correct(self.answers))
        print("Total questions:", self.question_count)

if __name__ == "__main__":
    Quiz(question_count=10).run()
