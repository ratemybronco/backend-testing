from flask import Flask, render_template
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

@app.route("/search")
def search():
  return "Search Request"

if __name__ == "__main__":
  app.run()