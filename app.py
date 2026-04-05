#imports Flask, allows referencing of Flask API. Imports random table for randomized variables.
from flask import Flask, render_template, jsonify, request, session
import random

app = Flask(__name__)
#Determines Session
app.secret_key = "secretkey" 

#defines symbols for game
symbols = ["Atlanta","Cincinnati","Detroit","Dallas","Denver"]

#Payouts
payouts = {
  "Atlanta": 2,
  "Cincinnati": 10,
  "Detroit": 2,
  "Dallas": 5,
  "Denver": 2
}

  #variable definition 
@app.route("/")
def index();
if "balance" not in session:
  session["balance"} = 1000
  return render_template("index.html", balance=session["balance"])

#betting parameters
@app.route("/spin", methods=["POST"])
def spin()
  bet = int(request.json.get("bet",0)
  if bet <= 0:
    return jsonify({"error": "Invalid bet"})
  
  if bet > session ["balance"]
    return jsonify({"error": "Not enough money"})

  #deducting bet from balance
  session["balance"] -= bet

  result = [random.choice(symbols) for _ range(3)

  win = False
  winnings = 0

#win circumstances, checking for a win
if result[0] == result [1] == result [2]
  win = true
  multiplier = payouts [result[0]]
  winnings = bet * multiplier
  session["balance"] += bet

return jsonify({
  "result":result,
  "balance": session["balance"],
  "win",
  "winnings": winnings
})

if __name__ =="__main__"
    import os
    port = int(os.environ.get("PORT", 3000)
    app.run(host="0.0.0.0", port=port)
