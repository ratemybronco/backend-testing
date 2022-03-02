from flask import Flask, redirect, render_template, request
import base64
from io import BytesIO
from matplotlib.figure import Figure
from IPython.display import display
from pymongo import MongoClient
import numpy as np
from sklearn.datasets import load_iris
import pandas as pd
import matplotlib as plt
import mysql.connector
from flask_debugtoolbar import DebugToolbarExtension
import os

# mongodb client
client = MongoClient(host="localhost", port=5000)

ratemybroncoDB = mysql.connector.connect(host="localhost", user="root", database="ratemybronco")
mycursor = ratemybroncoDB.cursor()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv("key")

app.debug = True

toolbar = DebugToolbarExtension(app)

@app.route("/")
def landing():
  return render_template("index.html")

@app.route("/professors")
def professors():
  mycursor.execute("SELECT * FROM Professor")
  myresult = mycursor.fetchall()
  for i in myresult:
    print(i)
        

@app.route("/courses")
def courses():
  return "Courses Page"

@app.route("/courses/ratings")
def ratings():
  return "Ratings Page"

@app.route("/grade-disbursements")
def grades():
  # Loading irirs dataset
  data = load_iris()
  df = pd.DataFrame(data.data,columns = data.feature_names)

  # Generate the  matplot figure **without using pyplot**.
  fig = Figure()
  ax = fig.subplots()
  grades = ['A', 'B', 'C', 'D', 'F']
  disbursements = [10, 18, 8, 5, 3]
  ax.bar(grades, disbursements, color=['red', 'orange', 'yellow', 'green', 'blue'])
  ax.set_xlabel("Grade Received")
  ax.set_ylabel("Number of Students")
  ax.set_title("[Prof Name], [Course Number], [Semester], [Year] Grade Disbursement")
  # Save it to a temporary buffer.
  buf = BytesIO()
  fig.savefig(buf, format="png")
  # Embed the result in the html output.
  data = base64.b64encode(buf.getbuffer()).decode("ascii")

  return f"Grade Disbursement Page {display(df)} <img src='data:image/png;base64,{data}'/>"

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