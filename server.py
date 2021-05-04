from bottle import route, run, view, static_file, redirect


class TodoItem:
    def __init__(self, description, unique_uid):
        self.description = description
        self.is_completed = False
        self.uid = unique_uid

    def __str__(self):
    	return self.description.lower()


tasks_db = {
	1: TodoItem("Read the book", 1),
	2: TodoItem("Sleep", 2),
}

@route("/static/<filename:path>")
def send_static(filename):
    return static_file(filename, root="static")


@route("/")
@view("index")
def index():
	tasks = tasks_db.values()
    return {"tasks": tasks}

@route("api/delete/<uid:int>")
def api_delete(uid):
	tasks_db.pop(uid)
	return redirect("/")

@route("api/complete/<uid:int>")
def api_comlete(uid):
	tasks_db[uid].is_completed = True
	return "Ok"


###
run(host="localhost", port=8080)
