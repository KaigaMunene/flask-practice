from . import app
from .model import Question
path = "api/v1/"

@app.route(f"/{path}/",)
def hello(): #root handler function
    return "Hello There, How are you ?"