#importing flask

from flask import *

#initialize flask app

app=Flask(__name__)

#creating routes

@app.route("/api/home")

#defining function

def home():
     #return"welcome to home api"

    return jsonify({"Message":"Welcome to home API"})



@app.route("/api/product")

def product():
     return jsonify({"Message":"Welcome to product API"})

#post method
@app.route("/api/calc",methods=['POST'])

def calc():
     num1=request.form["num1"]
     num2=request.form["num2"]

     sum=int(num1)+int(num2)
     return jsonify({"Answer":sum})

#simple interest

@app.route("/api/simpleinterest",methods=["POST"])

def simpleinterest():
     principle=request.form["principle"]
     rate=request.form["rate"]
     time=request.form["time"]
     
     simpleinterest=int(principle)*int(rate)*int(time)/100
     return jsonify({"Answer":simpleinterest})










#running the app

app.run(debug=True)

