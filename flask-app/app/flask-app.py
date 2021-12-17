from bmi import bmicalculator
from flask import Flask,jsonify,request


app=Flask("__name__")
@app.route('/',methods=["GET","POST"])

def get_input():
    """A function to send request through Flask, evaluate the request and provide the result"""
    packet=request.get_json(force=True)
    height=packet["height"]
    weight=packet["weight"]
    calculator=bmicalculator(height, weight)
    return jsonify(packet,calculator)

if __name__=="__main__":
    app.run()
