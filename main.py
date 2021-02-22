from src.question_model import Question
from src.data import question_data
from src.quiz_brain import QuizBrain
from src.ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

print("Quiz completed")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
