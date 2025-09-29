# quiz_module.py

class Quiz:
    def __init__(self):
        self.questions = [
            {"q": "What is Python?", "a": "A programming language"},
            {"q": "Who created Python?", "a": "Guido van Rossum"}
        ]
        self.score = 0

    def start_quiz(self):
        print("\n--- Quiz Started ---")
        for i, q in enumerate(self.questions):
            ans = input(f"Q{i+1}: {q['q']} ")
            if ans.strip().lower() == q['a'].lower():
                print("Correct!")
                self.score += 1
            else:
                print(f"Incorrect. Correct answer: {q['a']}")
        print(f"Your score: {self.score}/{len(self.questions)}")

# Demo usage
if __name__ == "__main__":
    quiz = Quiz()
    quiz.start_quiz()
