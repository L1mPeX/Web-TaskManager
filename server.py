from bottle import route, run, view


class TodoItem:
    def __init__(self, description):
        self.description = description
        self.is_completed = False

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root="static")


@route("/")
@view("index")
def index():
    tasks = [
        TodoItem("Read the book"),
        TodoItem("Write some code"),
        TodoItem("Have breakfast"),
    ]
    return {"tasks": tasks}



###
run(host="localhost", port=8080)
