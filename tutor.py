# tutor.py
import json

class AITutor:
    def _init_(self, name="AI Tutor"):
        self.name = name
        self.log_file = "questions_log.json"

    def get_response(self, question):
        question = question.lower()
        responses = {
            "hello": "Hello! How can I help you with your studies today?",
            "what is ai": "AI stands for Artificial Intelligence. It's the simulation of human intelligence in machines.",
        }
        response = responses.get(question, "Interesting question! Let's explore it together.")
        self.log_question(question, response)
        return response

    def log_question(self, question, response):
        try:
            with open(self.log_file, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        data.append({"question": question, "response": response})

        with open(self.log_file, "w") as f:
            json.dump(data, f, indent=2)

# Demo usage
if _name_ == "_main_":
    tutor = AITutor()
    print(tutor.get_response("hello"))