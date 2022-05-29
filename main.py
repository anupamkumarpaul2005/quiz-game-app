from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface
from data import question_data
import html

question_list = []
for question in question_data:
    question_text = html.unescape(question["question"])
    question_answer = question["correct_answer"]
    question_list.append(Question(question_text, question_answer))

interface = QuizInterface(QuizBrain(question_list))
