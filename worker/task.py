from flask import Flask, request
from app import Add, Multiply
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    result = Add.apply_async(args=(data['a'], data['b']), ignore_result=False)
    return {"result" : result.get()}

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.json
    result = Multiply.apply_async(args=(data['a'], data['b']), ignore_result=False)
    return {"result" : result.get()}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(5000 if os.getenv("APP_PORT") is None or os.getenv("APP_PORT") == "" else os.getenv("APP_PORT")), debug=True)