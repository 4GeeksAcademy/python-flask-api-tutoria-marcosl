from flask import Flask, jsonify, request

app = Flask(__name__)

some_data = {
    "name": "Bobby",
    "lastname": "Rixer"
}

todos = [
    {
        "label": "My first task",
        "done": False
    }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/')
def home():
    return jsonify(some_data)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json()

    # Agregar el nuevo todo a la lista
    todos.append(request_body)

    # Devolver la lista actualizada
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)