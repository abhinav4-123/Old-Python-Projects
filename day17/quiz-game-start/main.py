# quiz project , project 16 Day 17
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for question in question_data:
    new_q = Question(question['question'], question['correct_answer'])
    question_bank.append(new_q)

#ie. we are converting data available in string format to a format of objects which is very easy to access from here now
# e.g.
# print(question_bank[0].answer)
# print(question_bank)
# now, will se how to bring one of these and interact with user
quiz=QuizBrain(question_bank)
while (quiz.still_has_questions()):#if que still has que remaining
    quiz.next_question()
    # still_has_question = quiz.still_has_questions()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")