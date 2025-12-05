from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store todos (resets when app restarts)
todos = []
next_id = 1


@app.route("/")
def index():
    return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add():
    global next_id
    text = request.form.get("text", "").strip()

    if text:
        todos.append({
            "id": next_id,
            "text": text,
            "done": False
        })
        next_id += 1

    return redirect(url_for("index"))


@app.route("/toggle/<int:todo_id>", methods=["POST"])
def toggle(todo_id):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["done"] = not todo["done"]
            break
    return redirect(url_for("index"))


@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return redirect(url_for("index"))


if __name__ == "__main__":
    # 0.0.0.0 so it works inside Docker later
    app.run(host="0.0.0.0", port=5000, debug=True)
