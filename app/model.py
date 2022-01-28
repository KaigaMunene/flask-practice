class Questions:
    questions = []  # class attribute

    def __init__(self, question_id="", title="", question=""):
        self.title = title
        self.question = question
        self.question_id = question_id

    def add(self):
        self.questions.append(
            {"id": self.question_id, "title": self.title, "question": self.question}
        )
        return "Question successfully added"

    def get_all(self):
        return self.questions

    def get_one(self, question_id):
        for question in self.questions:
            if question["id"] == question_id:
                return question

    def delete_question(self, question_id):  # change to delete_question
        for question in self.questions:
            if question["id"] == question_id:
                index = self.questions.index(question)
                self.questions.pop(index)
                return "Question successfully deleted"

    def update_question(self, question_id):
        for question in self.questions:
            if question["id"] == question_id:
                question.update({"title": self.title, "question": self.question})
        return "Question updated successfully"


class Answers:
    answers = []

    def __init__(self, question_id="", answer_id="", answer=""):  # ?????
        self.question_id = question_id
        self.answer_id = answer_id
        self.answer = answer

    def add_answer(self):
        self.answers.append(
            {
                "question_id": self.question_id,
                "answer_id": self.answer_id,
                "answer": self.answer,
            }
        )
        return "Answer has been posted"

    def get_all_answers(self):
        return self.answers

    def get_one_answer(self, answer_id):
        for answer in self.answers:
            if answer["answer_id"] == answer_id:
                return answer

    def get_answers_by_question_id(self, question_id):
        for answer in self.answers:
            if answer["question_id"] == question_id:
                return self.answers
