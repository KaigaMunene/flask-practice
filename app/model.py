class Questions:
  questions = []
  def __init__(self, question_id="", title="", question=""):
      self.title = title
      self.question = question
      self.question_id = question_id

  def add(self):
    self.questions.append({
      "id": self.question_id,
      "title": self.title,
      "question": self.question

  })

  def get_all(self):
    return self.questions

  def get_one(self, question_id):
    for question in self.questions:
      if question["id"] == question_id:
        return question

class Answers:
  answers = []
  def __init__(self,question_id="", answer_id="", answer=""):
    self.question_id = question_id
    self.answer_id = answer_id
    self.answer = answer
  
  def add_answer(self):
    self.answers.append({
      "question_id": self.question_id,
      "answer_id": self.answer_id,
      "answer": self.answer
    })
    return {"message": "answer has been posted"}

  def get_all_answers(self):
    return self.answers
  
  def get_one_answer(self, answer_id):
    for answer in self.answers:
      if  answer["answer_id"] == answer_id:
        return self.answer


