class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list


    def next_question(self):
        error = 0
        while self.question_number < len(self.question_list):
            score = self.question_number - error
            current_question = self.question_list[self.question_number]
            self.question_number += 1
            tf = input(f'Q.{self.question_number}: {current_question.text}. True or False? ')
            if tf != current_question.answer:
                print("The answer is incorrect. ")
                error += 1
            else:
                score += 1
            print(f'Your current score is {score}/{self.question_number}')


