import hashlib

from flask import jsonify, request

from . import app
from .model import Answers, Questions

path = "/api/v1"

# have consistent route paths
# descriptive error messages


def generate_id(title):
    return hashlib.sha256(title.encode("utf-8")).hexdigest()


@app.route(
    f"{path}/",
)
def hello():  # root handler function
    return "Hello There, How are you ?"


@app.route(f"{path}/question", methods=["POST"])
def post_question():
    data = request.get_json()
    title = data.get("title")
    question = data.get("question")
    if not title:
        return jsonify({"message": "Invalid title enter a valid title"}), 400
    if not question:
        return jsonify({"message": "Invalid question, enter a valid question"}), 400
    auto_generate_id = generate_id(title)
    if Questions().get_one(auto_generate_id):
        return {"message": "The question exists, please check out the answers"}, 201
    question = Questions(auto_generate_id, title, question)
    question.add()
    return jsonify({"message": "Question posted successfully"}), 201


@app.route(f"{path}/question", methods=["GET"])
def get_all_questions():
    questions = Questions().get_all()
    return jsonify({"question": questions}), 200


@app.route(f"{path}/question/<string:question_id>", methods=["GET"])
def get_one_question(question_id):
    question = Questions().get_one(question_id)
    if question is None:
        return jsonify({"message": "Question not found"}), 404
    return jsonify({"question": question}), 200


@app.route(f"{path}/question/<string:question_id>", methods=["PUT"])
def update_a_question(question_id):
    data = request.get_json()
    title = data.get("title")
    question = data.get("question")
    if Questions().get_one(question_id) is None:
        return jsonify({"message": "Question not found"}), 404
    if not title:
        return jsonify({"message": "Invalid title enter a valid title"}), 400
    if not question:
        return jsonify({"message": "Invalid question, enter a valid question"}), 400

    question = Questions(title=title, question=question).update_question(question_id)
    return jsonify({"message": "question updated successfully"}), 200


@app.route(f"{path}/question/<string:question_id>", methods=["DELETE"])
def delete_question(question_id):
    if Questions().get_one(question_id) is None:
        return jsonify({"message": "Question not found"}), 404
    Questions().delete_question(question_id)
    return jsonify({"message": "Question successfully deleted"}), 204
