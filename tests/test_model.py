from pyexpat import model
import unittest
import uuid

from app.model import  Question

class TestModel(unittest.TestCase):
    def test_add_question_returns_correct(self,title,question):
        questions = []
        title = self.title
        question =self.question
        generate_id = uuid.uuid4()
        questions.append({generate_id,title,question})
test_class = TestModel()    
question = test_class.test_add_question_returns_correct()