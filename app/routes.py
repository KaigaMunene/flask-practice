import hashlib

from flask import jsonify, request

from . import app
from .model import Answers, Questions

path = "/api/v1"

# have consistent route paths
# descriptive error messages


def generate_id(title):
    return hashlib.sha256(title.encode("utf-8")).hexdigest()


def generate_answer_id(answer):
    return hashlib.sha256(answer.encode("utf-8")).hexdigest()


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

    qs = Questions()
    qs.add(auto_generate_id, title, question)
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

    Questions().update_question(question_id, title, question)
    return jsonify({"message": "question updated successfully"}), 200


@app.route(f"{path}/question/<string:question_id>", methods=["DELETE"])
def delete_question(question_id):
    if Questions().get_one(question_id) is None:
        return jsonify({"message": "Question not found"}), 404

    Questions().delete_question(question_id)
    return jsonify({"message": "Question successfully deleted"}), 204


@app.route(f"{path}/answer", methods=["POST"])
def post_answer():
    data = request.get_json()
    question_id = data.get("question_id")
    answer = data.get("answer")
    auto_generate_answer_id = generate_answer_id(answer)
    if not question_id:
        return (
            jsonify({"message": "Invalid question_id, enter a valid question_id"}),
            400,
        )
    if not answer:
        return jsonify({"message": "Invalid answer, enter a valid answer"}), 400
    answer = Answers(question_id, auto_generate_answer_id, answer)
    answer.add_answer()
    return jsonify({"message": "Answer posted successfully"}), 201


@app.route(f"{path}/answer/<string:answer_id>", methods=["GET"])
def get_answer(answer_id):
    answer = Answers().get_one_answer(answer_id)
    if answer is None:
        return jsonify({"message": "answer not found"}), 404
    return jsonify({"answer": answer}), 200


@app.route(f"{path}/answers", methods=["GET"])
def get_all_answers():
    answers = Answers().get_all_answers()
    return jsonify({"answer": answers})


@app.route(f"{path}/answers/<string:question_id>", methods=["GET"])
def get_all_answers_to_a_question(question_id):
    answers = Answers().get_answers_by_question_id(question_id)
    return jsonify({"answer": answers})


@app.route(f"{path}/answer/<string:answer_id>", methods=["PUT"])
def update_answer_to_a_question(answer_id):
    data = request.get_json()
    question_id = data.get("question_id")
    answer = data.get("answer")
    if Answers().get_one_answer(answer_id) is None:
        return jsonify({"message": "Answer not found"}), 404
    answer = Answers(question_id=question_id, answer=answer).update_answer(answer_id)
    return jsonify({"message": "answer updated successfully"}), 200


@app.route(f"{path}/answer/<string:answer_id>", methods=["DELETE"])
def delete_an_answer(answer_id):
    if Answers().get_one_answer(answer_id) is None:
        return jsonify({"message": "Answer not found"}), 404
    Answers().delete_answer(answer_id)
    return jsonify({"message": "Question successfully deleted"}), 204
