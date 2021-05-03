# server.py
from bottle import route, run, static_file, view


class TodoItem:
    def __init__(self, description):
        self.description = description
        self.is_completed = False

    def __str__(self):
        return self.description.lower()


@route("/static/<filename:path>")
def send_static(filename):
    return static_file(filename, root="static")


@route("/")
@view("index")
def index():
    tasks = [
        TodoItem("Read the book"),
        TodoItem("Write some code"),
    ]
    return {"tasks": tasks}


###
run(host="localhost", port=8080, autoreload=True)
