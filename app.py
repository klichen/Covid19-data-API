from operator import ne
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)


class TimeSeries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __rep__(self):
        return "<Task %r>" % self.id


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        task_content = request.form["content"]
        new_task = TimeSeries(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except:
            return "There was an issue adding your task"

    else:
        tasks = TimeSeries.query.order_by(TimeSeries.date_created).all()
        return render_template("index.html", tasks=tasks)

"""
@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    #task = Todo.query.get_or_404(id)

    if request.method == "POST":
        task.content = request.form["content"]

        try:
            db.session.commit()
            return redirect("/")
        except:
            return "Error updating task"
    else:
        return render_template("update.html", task=task)
"""


if __name__ == "__main__":
    app.run(debug=True)