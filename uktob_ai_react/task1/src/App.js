import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';
/*
Task 1: String Repeater..
required two input fields and a submit button.
The first input field should accept a string
The second should accept a number.
On clicking the submit button,
 "display the inputted string repeated the number of times
  specified in the second input field, in a new paragraph below the form."
 Ensure proper validation and error handling for
the inputs.

 */



function App() {

  const [inputString, setInputString] = useState('');
  const [repeatNumber, setRepeatNumber] = useState(1);

  const handleInputStringChange = (event) => {
    setInputString(event.target.value);
  };

  const handleRepeatNumberChange = (event) => {
    setRepeatNumber(parseInt(event.target.value));
  };
  const [result, setResult] = useState('');
  const [error, setError] = useState('');
  const handleSubmit = (event) => {
    event.preventDefault();
    if (!inputString.trim()) {
      // Validate the 1st input
      setError('Please enter a string.');
      setResult('');
    } else if (isNaN(repeatNumber) || repeatNumber <= 0) {
      // makking sure the input is a number and is positive
      setError('Please enter a valid positive number.');
      setResult('');
    } else {
      //use repaet function to repeat the string based on the repeat number
      setError('');
      setResult(inputString.repeat(repeatNumber));
    }
  };

  return (
    <div className="App">
        <h3>Simple String repeater using React - task1 </h3>
     <form onSubmit={handleSubmit}>

          <label>Input String</label>
          <input type="text" value={inputString} onChange={handleInputStringChange} />
          <label>Repeat Number</label>
          <input type="number" value={repeatNumber} onChange={handleRepeatNumberChange} />
        <button type="submit">Submit</button>
      </form>
      {error && <p className="error">{error}</p>}
      {result && <p className="result">{result}</p>}
    </div>
  );
}

export default App;
