import React from 'react';
import ChatInterface from './components/ChatInterface';
import { Container, Navbar } from 'react-bootstrap';
import './App.css';

function App() {
  return (
    <div className="App">
      <Navbar bg="dark" variant="dark" expand="lg" className="mb-3">
        <Container>
          <Navbar.Brand href="#home">
            🏢 Real Estate Analyst Chatbot
          </Navbar.Brand>
        </Container>
      </Navbar>
      
      <ChatInterface />
    </div>
  );
}

export default App;
