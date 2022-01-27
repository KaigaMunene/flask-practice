import unittest
from app import app
import json

from app.routes import generate_id



class TestRoute(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.path = "api/v1"
        self.headers = {"Content-Type":"application/json"}
        # self.test_data = {"title": "Name", "question":"What is your name"}
    
    def test_post_a_question(self):
        response = self.client.post(f"/{self.path}/question", data=json.dumps({"title":"Animals", "question":"Species of animals"}), headers=self.headers)
        self.assertEqual(response.status_code, 201)
        response_json_to_python = json.loads(response.get_data())
        self.assertEqual(response_json_to_python["message"], "Question posted successfully")
    
    def test_for_post_question_title(self):
        invalid_data ={"title":"","question":"What is a server"}
        response = self.client.post(f"/{self.path}/question", data=json.dumps(invalid_data), headers=self.headers)
        self.assertEqual(response.status_code, 400)
        return_response_in_python = json.loads(response.data)
        self.assertEqual(return_response_in_python["message"],"Invalid title enter a valid title")
    
    def test_for_post_question_question(self):
        invalid_data ={"title":"Coding","question":""}
        response = self.client.post(f"/{self.path}/question", data=json.dumps(invalid_data), headers=self.headers)
        self.assertEqual(response.status_code, 400)
        return_response_in_python = json.loads(response.data)
        self.assertEqual(return_response_in_python["message"],"Invalid question, enter a valid question")

    def post_a_question(self, info):
        self.client.post(f"/{self.path}/question", data=json.dumps(info), headers=self.headers)  
    
    def test_get_questions(self):
        self.post_a_question({"title":"name","question":"what is your name"})
        response = self.client.get(f"{self.path}/question", headers=self.headers)
        self.assertEqual(response.status_code, 200)
        return_response_in_python = json.loads(response.data)
        my_questions = return_response_in_python["question"]
        self.assertIsInstance(my_questions, list)
        self.assertEqual(len(my_questions), 2)
    
    def test_get_one_question(self):
        posted_question = {"title":"Program","question":"what is a program"}
        self.post_a_question(posted_question)
        generated_id = generate_id(posted_question["title"])
        response = self.client.get(f"{self.path}/question/{generated_id}", headers=self.headers)
        question = json.loads(response.data)["question"]
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(question, dict)
        self.assertEqual(question["title"], posted_question["title"])
        self.assertEqual(question["question"], posted_question["question"])
    
    def test_delete_question(self):
        posted_question = {"title":"Exam","question":"When are the exams?"}      
        self.post_a_question(posted_question)
        generated_id = generate_id(posted_question["title"])
        response = self.client.delete(f"{self.path}/question/{generated_id}", headers=self.headers)
        self.assertEqual(response.status_code, 204)