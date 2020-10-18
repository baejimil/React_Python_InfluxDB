import React from 'react';

function App() {
  return (
    <div>
      <form action='http://127.0.0.1:5000/' method='POST'>
        <input type='text' name='dummy' placeholder='Dummy Data' />
        <button type='submit'>Save</button>
      </form>
    </div>
  );
}

export default App;
