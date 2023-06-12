# uktob_ai_tasks
## Flask API
### API EndPoints Documentation
### Base URL
http://localhost:5000
### Task 1
### Endpoints
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


### Task 2
### Endpoints
#### 1. Register user
The endpoint accept a post request with JSON object containing username and password

    Endpoint: /register

    Method: POST

    Request Body: JSON object with a "username" and 'password"  keys

    Example: {"username": 'Ahmed' , "password":1234}

    Response: JSON object with a success message the user is registered successfully.
  
#### Error Handling:
If the "username" or 'password" keys is missing in the JSON object, an error message is returned with status code 400.
if the user already a JSON object return indicating the user already exists .
#### 2. LogIn
The endpoint accept a post request with JSON object containing username and password

   Endpoint: /login

    Method: POST

    Request Body: JSON object with a "username" and 'password"  keys

    Example: {"username": 'Ahmed' , "password":1234}

    Response: JSON object with a success message the user granted the permission to login.
  
#### Error Handling:
If the "username" or 'password" keys is missing in the JSON object, an error message is returned with status code 400.
if the user not register or password is wrong a message returned with permission denied.


#### Test the Endpoint
using Postman to send POST requests with the appropriate JSON object to the respective endpoints and test the APIs.

#### Run The app
head over uktop_ai_flask directory, then run the command 

   pip install requirements
   
  in order to test the task, run 
  
  python app.py
  
  for the second task run 
  
  python authenticate.py
  
 ## React Task.
 The React apps is a simple frontend applications.divide into 
 ### task 1
 String Repater app is to allow the user input a string value "needed to be repeated" and a number value , that used to repeat the string 
 
 ### task 2 
 a simple to do list allow user to add tasks and delete them.
 
 ##### both apps includes form validation and error handling.
 
##### in order to run the first task
head over teh directroy uktob_ai_react/task2 
then run the following commands
  npm install 
  
  npm start
  
 the head over the  http://localhost:3000/ , an start validatiting the inputs. by entring a string and teh reptead string will be rendered.
 

 ##### in order  to run the second task
 head over teh directroy uktob_ai_react/task2
`then run the following commands
  npm install 
  npm start
 the head over the  http://localhost:3000/  and start adding task and delete them.
