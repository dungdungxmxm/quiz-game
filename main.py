from data import question_data
from question_model import Question
from quiz_brain import Quiz

questions = [Question(item["question"], item["correct_answer"]) for item in question_data]

quiz = Quiz(questions)

while quiz.still_has_questions():
    user_answer = quiz.next_question()
    quiz.checking_answer(user_answer, questions[quiz.question_number-1].answer)
    print("\n")

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(questions)}")