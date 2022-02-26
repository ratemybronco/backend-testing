from flask import Flask, redirect, render_template, request
from pymongo import MongoClient

# mongodb client
client = MongoClient(host="localhost", port=5000)

app = Flask(__name__)

@app.route("/")
def landing():
  return render_template("index.html")

@app.route("/professors")
def professors():
  return "Professors Page"

@app.route("/courses")
def courses():
  return "Courses Page"

@app.route("/courses/ratings")
def ratings():
  return "Ratings Page"

@app.route("/grade-disbursements")
def grades():
  return "Grade Disbursement Page"

names = [] # To be replaced with database access
@app.route("/search", methods=["GET","POST"])
def search():
  if request.method == "GET":
    return render_template("search.html", professors=names)
    
  professor = request.form.get("professor")
  if not professor:
    return "output blank"
  names.append(professor)
  return redirect("/search")
  #return redirect(f"/result/{professor}")

@app.route("/result/<name>", methods=["GET"])
def result(name):
  return render_template("result.html", name=name)

if __name__ == "__main__":
  app.run()