#imports Flask, allows referencing of Flask API. Imports random table for randomized variables.
from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

#defines symbols for game
symbols = ["Atlanta","Cincinnati","Detroit","Dallas","Denver"]

#variable definition 
@app.route("/")
def index();
  return render_template("index.html")

@app.route("/spin")
def spin()
  result = [random.choice(symbols) for _ range(3)
  return jsonify(result)

if __name__ =="__main__"
    app.run(host="0.0.0.0", port=3000)
