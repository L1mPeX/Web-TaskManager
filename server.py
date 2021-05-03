from bottle import route, run, view, static_file, redirect, request


class TodoItem:
    def __init__(self, description):
        self.description = description
        self.is_completed = False

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root="static")

@route("/add-tesk", method="POST")
def add_task():
    desc = request.POST.description.strip()
    if len(desc) > 0:
        new_uid = max(tasks_db.keys()) + 1
        t = TodoItem(desc, new_uid)
        tsks_db[new_uid] = t
    return redirect("/")



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
