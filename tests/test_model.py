from app import model
import unittest
from app.model import  Questions, Answers

# test setUp method
class TestQuestions(unittest.TestCase):
    def test_add_question_returns_correct(self):
        self.assertEqual(Questions(1,"class","what is a class").add(),"Question successfully added")

    def test_get_all_questions_is_correct(self):
        self.assertEqual(Questions(1,"class","What is a class").get_all(), [{"id":1,"title":"class","question":"what is a class"}])
    
    def test_get_one_question(self):
        self.assertEqual(Questions().get_one(1),{"id":1,"title":"class","question":"what is a class"})
    
    def test_remove_a_question(self):
        self.assertEqual(Questions().remove_question(1), "Question successfully deleted")
    
    def test_to_update_a_question(self):
        self.assertEqual(Questions(title="html", question="how to right a div").update_question(1), "Question updated successfully")

class TestAnswers(unittest.TestCase):
    def test_add_answers(self):
        answers = Answers(1,1,"A class is a blueprint of an object")
        result = answers.add_answer()
        self.assertEqual("Answer has been posted", result)
    
    def test_get_all_answers(self):
        self.assertEqual(Answers().get_all_answers(), [{"question_id" : 1, "answer_id" : 1,"answer":"A class is a blueprint of an object"}])
        self.assertIsInstance(Answers().get_all_answers(), list)

    def test_get_one_answer(self):
        self.assertEqual(Answers().get_one_answer(1),{"question_id" : 1, "answer_id" : 1,"answer":"A class is a blueprint of an object"})
        
if __name__ == "__main__":
  unittest.main()