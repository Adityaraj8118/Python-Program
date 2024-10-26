class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run(self):
        for question in self.questions:
            user_answer = input(question.prompt + " ")
            if user_answer.lower() == question.answer.lower():
                self.score += 1
                print("Correct!")
            else:
                print("Incorrect.")
        print(f"You scored {self.score}/{len(self.questions)}.")

questions = [
    Question("What is the capital of France? ", "Paris"),
    Question("What is 2 + 2? ", "4"),
    Question("What is the capital of Japan? ", "Tokyo"),
]

quiz = Quiz(questions)
quiz.run()