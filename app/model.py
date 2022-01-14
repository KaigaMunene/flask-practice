class Question:
    questions = []
    def __init__(self, title, question):
        self.title = title
        self.question = question

    def add(self):
      self.questions.append({
        "id": len(self.questions),
        "question": self.question,
        "title": self.title
      })

    def get_all(self):
      return self.questions


    def get_one(self, id):
      return list(filter(lambda query:query["id"] == id, self.questions))[0]

