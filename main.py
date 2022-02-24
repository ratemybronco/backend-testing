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

if __name__ == "__main__":
  app.run()