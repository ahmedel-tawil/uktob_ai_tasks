from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('flask_task1.html')


@app.route('/calculate_sum', methods=['POST'])
def calculate_sum():
    """
    The endpoint is to take a JSON object containing a list of numbers
    i.e: {
          "numbers_list": [6, 7, 9,10, 20]
        }

    :return JSON object with a "summation_of_numbers" key containing the sum of the numbers.
    """
    data = request.get_json()
    if not data:
        return jsonify(
            {'error': 'No input provided, please provide the input in form of JSON object with key numbers_list'
                      'and the value to be a list of numbers '}), 400

    try:
        numbers = data['numbers_list']
    except KeyError:
        return jsonify(
            {'error': "please provide the JSON object with key 'numbers_list'"}), 400
    # validate the input data, 1- input is a list , 2- the list contains only numbers "int or float"
    if isinstance(numbers, list):
        if all(isinstance(number, (int, float)) for number in numbers):
            summation_of_numbers = sum(numbers)
            return jsonify({'sum': summation_of_numbers}), 200
        return jsonify({'error': 'Invalid input. Expected a list of numbers.'}), 400  # list should contain only numbers
    return jsonify({'error': 'Invalid input. Expected a list of numbers.'}), 400  # should be a list..



@app.route('/concatenate_strings', methods=['POST'])
def concatenate_strings():
    """
    The endpoint is accepting a JSON object containing two strings return the concatenated result.
    i.e: {
          "string1": "Ahmed",
          "string2": "El-tawil"
        }

    :return concatenated_string
    """
    data = request.get_json()
    if not data:
        return jsonify(
            {'error': "No input provided, please provide the input in form"
                      "of JSON object with two keys 'string1', 'string2'"}), 400

    if 'string1' not in data or 'string2' not in data:
        return jsonify(
            {'error': "please provide the JSON object with two keys 'string1', 'string2'"}), 400
    string1 = data['string1']
    string2 = data['string2']
    if isinstance(string1, str) and isinstance(string2, str):
        concatenated_string = string1 + string2
        return jsonify({'result': concatenated_string})
    return jsonify({'error': 'Invalid input. Expected two strings input type'}), 400



@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Endpoint not found.'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal server error.'}), 500
if __name__ == '__main__':
    app.run()
