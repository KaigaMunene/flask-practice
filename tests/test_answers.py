import json
import pdb
import unittest

from app import app
from app.routes import generate_id


class TestAnswersRoutes(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.path = "/api/v1"
        self.headers = {"Content-Type": "application/json"}

    def post_a_question(self, data):
        self.client.post(
            f"{self.path}/question", data=json.dumps(data), headers=self.headers
        )

    def post_an_answer(self, info):
        self.client.post(
            f"{self.path}/answer", data=json.dumps(info), headers=self.headers
        )

    def test_post_answers(self):
        post_question = {
            "title": "Python",
            "question": "What are the various Datatypes of python",
        }
        self.post_a_question(post_question)

        generated_id = generate_id(post_question["title"])

        response = self.client.post(
            f"{self.path}/answer",
            data=json.dumps(
                {
                    "question_id": generated_id,
                    "answer": "The various datatypes are integers,boolean,string,float,dictionary,sets,lists and tuples",
                }
            ),
            headers=self.headers,
        )

        response_data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_data.get("message"), "Answer posted successfully")

    def test_post_answer_without_question_id_field(self):
        post_question = {
            "title": "Network",
            "question": "What are network systems?",
        }
        self.post_a_question(post_question)

        answer = {
            "question_id": "",
            "answer": "A network ensure connectivity between users or various devices.",
        }
        response = self.client.post(
            f"{self.path}/answer", data=json.dumps(answer), headers=self.headers
        )
        res_data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            res_data["message"], "Invalid question_id, enter a valid question_id"
        )

    def test_post_answer_without_answer_field(self):
        post_question = {
            "title": "Python",
            "question": "What are the various Datatypes of python",
        }
        self.post_a_question(post_question)

        generated_id = generate_id(post_question["title"])
        answer = {"question_id": generated_id, "answer": ""}
        response = self.client.post(
            f"{self.path}/answer", data=json.dumps(answer), headers=self.headers
        )
        res_data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(res_data["message"], "Invalid answer, enter a valid answer")

    def test_get_answer_for_one_question(self):
        posted_question = {
            "title": "Django",
            "question": "What is Django and why we use it ?",
        }
        self.post_a_question(posted_question)

        generated_id = generate_id(posted_question["title"])

        posted_answer = {
            "question_id": generated_id,
            "answer": "Django is a high-level Python web framework that enables rapid development of secure and maintainable websites.",
        }
        self.post_an_answer(posted_answer)

        generated_answer_id = generate_id(posted_answer["answer"])

        response = self.client.get(
            f"{self.path}/answer/{generated_answer_id}", headers=self.headers
        )

        res_data = json.loads(response.data)
        answer = res_data["answer"]
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(answer, dict)

    def test_get_answer_without_answer_id(self):
        posted_question = {
            "title": "React",
            "question": "What is React and why we use it ?",
        }
        self.post_a_question(posted_question)

        generated_id = generate_id(posted_question["title"])

        posted_answer = {
            "question_id": generated_id,
            "answer": "Django is a high-level Python web framework that enables rapid development of secure and maintainable websites.",
        }
        self.post_an_answer(posted_answer)

        response = self.client.get(f"{self.path}/answer/1", headers=self.headers)

        res_data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(res_data["message"], "answer not found")

    def test_get_all_answers(self):
        posted_question = {
            "title": "Heroku",
            "question": "What is Heroku and why we use it ?",
        }
        self.post_a_question(posted_question)

        generated_id = generate_id(posted_question["title"])
        self.post_an_answer(
            {
                "question_id": generated_id,
                "answer": "Heroku is a platform, as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.",
            }
        )

        response = self.client.get(f"{self.path}/answers", headers=self.headers)
        res_data = json.loads(response.data)
        answers = res_data["answer"]
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(answers, list)

    def test_get_all_answers_to_a_question(self):
        posted_question = {
            "title": "Github",
            "question": "What is github and what it is used for ?",
        }
        self.post_a_question(posted_question)
        generated_question_id = generate_id(posted_question["title"])
        self.post_an_answer(
            {
                "question_id": generated_question_id,
                "answer": "Github is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.",
            }
        )
        response = self.client.get(
            f"{self.path}/answers/{generated_question_id}", headers=self.headers
        )
        res_data = json.loads(response.data)
        answers = res_data["answer"]
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(answers, list)

    def test_update_answer(self):
        posted_question = {
            "title": "Docker",
            "question": "What is docker and what is it used for ?",
        }
        self.post_a_question(posted_question)

        generated_question_id = generate_id(posted_question["title"])

        post_answer = {
            "question_id": generated_question_id,
            "answer": "Docker is an open source containerization platform. It enables developers to package applications into containers—standardized executable components combining application source code with the operating system (OS) libraries and dependencies required to run that code in any environment.",
        }
        self.post_an_answer(post_answer)

        generated_answer_id = generate_id(post_answer["answer"])

        response = self.client.put(
            f"{self.path}/answer/{generated_answer_id}",
            data=json.dumps(post_answer),
            headers=self.headers,
        )
        response_data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data["message"], "answer updated successfully")

    def test_to_try_to_update_answer_which_doesnot_exist(self):
        posted_question = {"title": "Human", "question": "What is a human being?"}
        self.post_a_question(posted_question)

        generated_id = generate_id(posted_question["title"])

        posted_answer = {
            "question_id": generated_id,
            "answer": "A human is a living being.",
        }
        self.post_an_answer(posted_answer)
        response = self.client.put(
            f"{self.path}/answer/1",
            data=json.dumps(posted_answer),
            headers=self.headers,
        )

        response_data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_data["message"], "Answer not found")


    def test_delete_answer(self):
        posted_question = {
            "title": "Politics",
            "question": "What is the political situation in Kenya?",
        }
        self.post_a_question(posted_question)

        generated_id = generate_id(posted_question["title"])

        posted_answer = {
            "question_id": generated_id,
            "answer": "It's near the time for elections and tensions are arising",
        }
        self.post_an_answer(posted_answer)
        generated_answer_id = generate_id(posted_answer["answer"])
        response = self.client.delete(
            f"{self.path}/answer/{generated_answer_id}", headers=self.headers
        )
        self.assertEqual(response.status_code, 204)

    def test_delete_answer_which_doesnot_exist(self):
        posted_question = {"title": "Gender", "question": "What is your gender?"}
        self.post_a_question(posted_question)

        generated_id = generate_id(posted_question["title"])

        posted_answer = {"question_id": generated_id, "answer": "My gender is male."}
        self.post_an_answer(posted_answer)
        response = self.client.delete(
            f"{self.path}/answer/1",
            data=json.dumps(posted_answer),
            headers=self.headers,
        )

        response_data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_data["message"], "Answer not found")
