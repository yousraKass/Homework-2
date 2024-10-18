from flask import Flask, jsonify
from Division import Division
from Addition import Addition
from multiplication import Multiplication
from Subtraction import Subtraction

app = Flask(__name__)


@app.route('/add/<int:a>/<int:b>', methods=['GET'])
def add(a,b):
    return jsonify({'status': 200, 'result': Addition.compute(a,b)})

@app.route('/subtract/<int:a>/<int:b>', methods=['GET'])
def subtract(a,b):
    return jsonify({'status': 200, 'result': Subtraction.compute(a,b)})


@app.route('/multiply/<int:a>/<int:b>', methods=['GET'])
def multiply(a,b):
    return jsonify({'status': 200, 'result': multiplication.compute(a,b)})

@app.route('/divide/<int:a>/<int:b>', methods=['GET'])
def divide(a,b):
    return jsonify({'status': 200, 'result': Division.compute(a,b)})
