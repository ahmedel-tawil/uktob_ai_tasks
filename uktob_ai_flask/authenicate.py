from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

"""
Question 2
Implement a simple user authentication system using Flask. Create an endpoint for user registration that accepts a
username and password, stores them in a dictionary (as a stand-in for a real database)  #users_dict#, and returns a success message.
Then create an endpoint for user login that checks if the provided username and password match the stored values, and
if so, returns an "access granted" message; otherwise, return an "access denied" message.

"""
users_dict = {}


@app.route('/')
def hello():
    return render_template('flask_task2.html')


@app.route('/register', methods=['POST'])
def register():
    """
    The endpoint is to take a JSON object holding username and password to register a newuser.
    :return success message if the user registered successfully, otherwise return error message:
    """
    data = request.get_json()
    if not data:
        return jsonify(
            {'error': "No input provided, please provide the input in form"
                      "of JSON object with two keys 'username', 'password'"}), 400

    if 'username' not in data or 'password' not in data:
        return jsonify(
            {'error': "please provide the JSON object with keys 'username', 'password'"}), 400
    username = data['username']
    password = data['password']
    if username in users_dict:
        return jsonify({'error': 'username already exists'}), 400
    users_dict[username] = password
    return jsonify({'message': 'user registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
    """
       The endpoint is to take a JSON object holding username and password to login an existing .
       :return success message if the user granted the permission, otherwise return error message:
       """
    data = request.get_json()
    if not data:
        return jsonify(
            {'error': "No input provided, please provide the input in form"
                      "of JSON object with two keys 'username', 'password'"}), 400
    if 'username' not in data or 'password' not in data:
        return jsonify(
            {'error': "please provide the JSON object with keys 'username', 'password'"}), 400
    username = data['username']
    password = data['password']
    if username in users_dict and users_dict[username] == password:
        return jsonify({'success': "access granted"}), 200
    return jsonify({'message': "access denied"}), 400


@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Endpoint not found.'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal server error.'}), 500

if __name__ == '__main__':
    app.run()
