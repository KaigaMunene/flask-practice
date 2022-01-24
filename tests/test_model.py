from app import model
import unittest
from app.model import  Questions, Answers
class TestQuestions(unittest.TestCase):
    def test_add_question_returns_correct(self):
        self.assertEqual(Questions(1,"class","what is a class").add(),"Question successfully added")

    def test_get_all_questions_is_correct(self):
        self.assertEqual(Questions(1,"class","What is a class").get_all(), [{"id":1,"title":"class","question":"what is a class"}])

class TestAnswers(unittest.TestCase):
    def test_add_answers(self):
        answers = Answers(1,1,"A class is a blueprint of an object")
        result = answers.add_answer()
        self.assertEqual("Answer has been posted", result)
    
    def test_get_all_answers(self):
        self.assertEqual(Answers(1,1,"A class is a blueprint of an object").get_all_answers(), [{"question_id" : 1, "answer_id" : 1,"answer":"A class is a blueprint of an object"}])

    # def test_get_one_answer(self,answer_id):
    #     answer = Answers()
    #     result = answer.get_one_answer(answer_id)
    #     self.assertEqual(id , result)
if __name__ == "__main__":
  unittest.main()