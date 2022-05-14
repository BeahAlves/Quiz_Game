from data import question_data
from question_model import Question
from OOP import QuizBrain

question_bank = []

for question in question_data:
    question_text = question['question']  # Tem todas as perguntas
    question_answer = question['correct_answer']  # Tem todas as respostas
    new_question = Question(question_text, question_answer)

    question_bank.append(new_question)

quizbrain = QuizBrain(question_bank)
quizbrain.next_question()