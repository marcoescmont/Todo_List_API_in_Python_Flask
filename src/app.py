import json
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = json.loads(request.data)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos', methods=['PUT'])
def update_todo():
    global todos
    incoming_todos = json.loads(request.data)
    todos = incoming_todos
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[position]
    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)