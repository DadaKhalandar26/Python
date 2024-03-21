from Day_17_Quiz_Game.question_model import Question
from quiz_brain import QuizzBrain
from data import question_data, new_questions_data


question_bank = []
for items in new_questions_data:
    question_text = items["question"]
    question_answer = items["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizzBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")