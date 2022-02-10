import unittest

from app.model import Answers, Questions


class TestQuestions(unittest.TestCase):
    def setUp(self):
        self.question = {
            "question_id": 1,
            "title": "class",
            "question": "what is a class",
        }

    def test_add_question_returns_correct(self):
        qs = Questions()
        response = qs.add(
            self.question["question_id"],
            self.question["title"],
            self.question["question"],
        )
        self.assertEqual(response, "Question successfully added")

    def test_get_all_questions_is_correct(self):
        qs = Questions()
        previous_count = len(qs.get_all())

        qs.add(
            2,
            self.question["title"],
            self.question["question"],
        )

        current_count = len(qs.get_all())

        self.assertEqual(current_count, previous_count + 1)

    def test_get_one_question(self):
        qs = Questions()
        question = qs.get_one(self.question["question_id"])

        self.assertEqual(question["id"], self.question["question_id"])
        self.assertEqual(question["title"], self.question["title"])
        self.assertEqual(question["question"], self.question["question"])

    def test_delete_a_question(self):
        question = {
            "question_id": 3,
            "title": "Test",
            "question": "This is a test question",
        }
        qs = Questions()
        qs.add(question["question_id"], question["title"], question["question"])
        previous_count = len(qs.get_all())

        # delete question added
        response = qs.delete_question(question["question_id"])
        current_count = len(qs.get_all())
        self.assertEqual(response, "Question successfully deleted")
        self.assertEqual(current_count, previous_count - 1)

    def test_to_update_a_question(self):
        self.assertEqual(
            Questions().update_question(1, "html", "how to right a div"),
            "Question updated successfully",
        )

class TestAnswers(unittest.TestCase):
    def test_add_answers(self):
        answers = Answers(1, 1, "A class is a blueprint of an object")
        result = answers.add_answer()
        self.assertEqual("Answer has been posted", result)

    def test_get_all_answers(self):
        self.assertNotEqual(len(Answers().get_all_answers()), 0)

        self.assertIsInstance(Answers().get_all_answers(), list)

    def test_get_one_answer(self):
        self.assertEqual(
            Answers().get_one_answer(1),
            {
                "question_id": 1,
                "answer_id": 1,
                "answer": "A class is a blueprint of an object",
            },
        )


if __name__ == "__main__":
    unittest.main()
