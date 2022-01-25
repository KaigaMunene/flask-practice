from crypt import methods
from . import app 
from .model import Questions, Answers
from flask import request,jsonify
import uuid
path = "api/v1/"

# have consistent route paths
# descriptive error messages

@app.route(f"/{path}/",) 
def hello(): #root handler function
    return "Hello There, How are you ?"

@app.route(f"/{path}/question", methods= ["POST"])
def post_question():
    data = request.get_json()
    title = data.get("title")
    question = data.get("question")
    if not title : 
        return jsonify({"message":"enter title"})
    if not question:
        return jsonify({"message": "enter question"})
    auto_generate_id = str(uuid.uuid4())
    question = Questions(auto_generate_id,title,question)
    question.add()
    return jsonify({"message":"Question posted successfully"}), 201

@app.route(f"/{path}/question", methods = ["GET"])
def get_all_questions():
    questions = Questions().get_all()
    return jsonify({"question": questions}), 200


@app.route(f"/{path}/question/<string:question_id>", methods = ["GET"])
def get_one_question(question_id):
    question = Questions().get_one(question_id)
    return jsonify({"question": question}), 200



