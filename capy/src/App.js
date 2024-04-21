import React from 'react';
import { BrowserRouter as Router, Route, Routes, redirect} from 'react-router-dom';

import ToDoList from './components/todo'
import Navigation from './components/navigation';

//TODO: set default to chat app

function App() {
  return (
    <Router>
      <div>
        <Navigation />
        <Routes>
          <Route path="/todo" element={<ToDoList/>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;