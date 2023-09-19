from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample user information
user_info = {
    "user_id": "john_doe_17091999",
    "email": "john@xyz.com",
    "roll_number": "ABCD123"
}

@app.route('/bfhl', methods=['POST'])
def bfhl_post():
    try:
        data = request.json.get('data', [])
        numbers = [x for x in data if x.isdigit()]
        alphabets = [x for x in data if x.isalpha()]
        highest_alphabet = [max(alphabets, key=lambda x: x.lower())] if alphabets else []

        response = {
            "is_success": True,
            **user_info,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def bfhl_get():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
