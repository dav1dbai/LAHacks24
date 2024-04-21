import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import Todo from './components/todo'
//import Chatbot from './components/Chatbot'
import Calendar from './components/calendar'
import Navigation from './components/navigation';

function App() {
  return (
    <Router>
      <div>
        <Navigation />
        <Routes>
          <Route path="/todo" element={<Todo/>} />
          <Route path="/chat" element={<Todo/>}/>
          <Route path="/cal" element={<Calendar/>}/>
        </Routes>
      </div>
    </Router>
  );
}

export default App;