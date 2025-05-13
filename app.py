from flask import Flask, render_template, request, redirect, url_for, abort

import random

app = Flask(__name__)

# In-memory storage (will reset on restart)
tasks = []
total_points = 0
coins = 0

@app.route("/", methods=["GET", "POST"])
def index():
    global tasks

    if request.method == "POST":
        task_text = request.form.get("task")
        points = request.form.get("points")

        if task_text and points and points.isdigit():
            tasks.append({
                "task": task_text,
                "points": int(points),
                "completed": False
            })
        return redirect(url_for("index"))

    pending_tasks = [t for t in tasks if not t["completed"]]
    completed_tasks = [t for t in tasks if t["completed"]]

    result = request.args.get("result")  # game result messages

    return render_template("index.html", tasks=pending_tasks, completed=completed_tasks,
                           total_points=total_points, coins=coins, result=result)


@app.route("/complete/<int:task_id>")
def complete(task_id):
    global total_points

    if 0 <= task_id < len(tasks):
        task = tasks[task_id]
        if not task["completed"]:
            task["completed"] = True
            total_points += task["points"]
        return redirect(url_for("index"))
    else:
        abort(404)


@app.route("/delete/<int:task_id>")
def delete(task_id):
    global total_points

    if 0 <= task_id < len(tasks):
        task = tasks.pop(task_id)
        if task["completed"]:
            total_points -= task["points"]
        return redirect(url_for("index"))
    else:
        abort(404)


@app.route("/exchange_points", methods=["POST"])
def exchange_points():
    global total_points, coins
    if total_points >= 100:
        coins += total_points // 100
        total_points %= 100
    return redirect(url_for("index"))


@app.route("/gamble", methods=["POST"])
def gamble():
    global coins

    if coins >= 1:
        coins -= 1
        if random.choice([True, False]):
            coins += 3
            result = "🎉 You won 3 coins!"
        else:
            result = "💩 You lost 1 coin."
    else:
        result = "Not enough coins to gamble."

    return redirect(url_for("index", result=result))


@app.route("/dice_roll", methods=["POST"])
def dice_roll():
    global coins

    if coins >= 2:
        coins -= 2
        roll = random.randint(1, 6)

        if roll == 6:
            coins += 5
            result = "👑 You rolled a 6! You win 5 coins!"
        elif roll >= 4:
            coins += 3
            result = f"🎉 You rolled a {roll}! You win 3 coins!"
        else:
            result = f"💩 You rolled a {roll}. You lost your 2 coins."
    else:
        result = "Not enough coins to roll the dice."

    return redirect(url_for("index", result=result))


if __name__ == "__main__":
    app.run(debug=True)
