class Quiz:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def still_has_questions(self):
        length = len(self.questions_list)
        if self.question_number < length:
            return True
        return False

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        return input(f"Q.{self.question_number}: {current_question.text} (True/False): ")

    def checking_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_ans}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")