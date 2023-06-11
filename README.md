# uktob_ai_tasks
# Task1 Flask API
Task 1
API EndPoints Documentation
Base URL
http://localhost:5000

Endpoints
1. Calculate Sum of Given list of Numbers
The endpoint accept a post request with JSON object containing a list of numbers
    Endpoint: /calculate_sum
    Method: POST
    Request Body: JSON object with a "numbers_list" key containing a list of numbers.
    Example: {"numbers_list": [6, 7, 9,10, 20]}
    Response: JSON object with a "summation_of_numbers" key containing the sum of the numbers.
 
Error Handling:

If the "numbers_list" key is missing in the JSON object, an error message is returned with status code 400.
If the value of "numbers_list" is not a list of numbers, an error message is returned with status code 400.
2. Concatenate Strings
This endpoint accepts a JSON object containing two strings and returns their concatenated result.

    Endpoint: /concatenate

    Method: POST

    Request Body: JSON object with a "string1" key and a "string2" key containing two strings.

    Example: {"string1": "Hello, ", "string2": "World!"}

    Response: JSON object with a "result" key containing the concatenated string.
  
Error Handling:

If either "string1" or "string2" key is missing in the JSON object, an error message is returned with status code 400.
