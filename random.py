class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.current_question = 0

    def display_question(self):
        question = self.questions[self.current_question]
        print(question["question"])

        for i, option in enumerate(question["options"], start=1):
            print(f"{i}. {option}")

    def check_answer(self, user_answer):
        correct_answer = self.questions[self.current_question]["correctAnswer"]
        if user_answer == correct_answer:
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}\n")

        self.current_question += 1

    def run_quiz(self):
        for _ in range(len(self.questions)):
            self.display_question()
            user_answer = input("Your answer: ")
            self.check_answer(user_answer)

        print(f"Quiz completed! Your final score is: {self.score}/{len(self.questions)}")


# Sample quiz data
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "Berlin", "London", "Madrid"],
        "correctAnswer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "correctAnswer": "Mars"
    }
    # Add more questions as needed
]

# Create a Quiz instance and run the quiz
quiz = Quiz(questions)
quiz.run_quiz() 
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.current_question = 0

    def display_question(self):
        question = self.questions[self.current_question]
        print(question["question"])

        for i, option in enumerate(question["options"], start=1):
            print(f"{i}. {option}")

    def check_answer(self, user_answer):
        correct_answer = self.questions[self.current_question]["correctAnswer"]
        if user_answer == correct_answer:
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}\n")

        self.current_question += 1

    def run_quiz(self):
        for _ in range(len(self.questions)):
            self.display_question()
            user_answer = input("Your answer:")
            self.check_answer(user_answer)

        print(f"Quiz completed! Your final score is: {self.score}/{len(self.questions)}")


# Sample quiz data
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "Berlin", "London", "Madrid"],
        "correctAnswer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "correctAnswer": "Mars"
    },
     {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "correctAnswer": "Blue Whale"
    },
    {
        "question": "In which year did the Titanic sink?",
        "options": ["1910", "1912", "1920", "1935"],
        "correctAnswer": "1912"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
        "correctAnswer": "William Shakespeare"
    },
    {
        "question": "Which country is known as the 'Land of the Rising Sun'?",
        "options": ["China", "Japan", "South Korea", "Vietnam"],
        "correctAnswer": "Japan"
    },
    {
        "question": "What is the capital of Australia?",
        "options": ["Sydney", "Melbourne", "Canberra", "Perth"],
        "correctAnswer": "Canberra"
    }
]

    # Add more questions as needed


# Create a Quiz instance and run the quiz
quiz = Quiz(questions)
quiz.run_quiz()