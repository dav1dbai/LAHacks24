import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import Todo from './components/todo'
import Navigation from './components/navigation';

function App() {
  return (
    <Router>
      <div>
        <Navigation />
        <Routes>
          <Route path="/todo" element={<Todo/>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;