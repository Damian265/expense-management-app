from flask import Flask, jsonify, request

app = Flask(__name__)
expenses = []

@app.route('/')
def home():
    return "Welcome to the Expense Management App!"

@app.route('/add_expense', methods=['POST'])
def add_expense():
    data = request.json
    expenses.append(data)
    return jsonify({"message": "Expense added successfully!"}), 201

@app.route('/expenses', methods=['GET'])
def get_expenses():
    return jsonify(expenses), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
