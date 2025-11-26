import React, { useState, useEffect, useRef } from 'react';
import { Container, Form, Button, InputGroup, Spinner } from 'react-bootstrap';
import MessageDisplay from './MessageDisplay';
import { queryAnalysis } from '../services/apiService';

const ChatInterface = () => {
  const [messages, setMessages] = useState([
    {
      type: 'bot',
      summary: "**Welcome to Real Estate Analyst!**\n\nI can help you analyze real estate trends in Pune. Try asking:\n\n* \"Give me analysis of Wakad\"\n* \"Compare Ambegaon Budruk and Aundh demand trends\"\n* \"Show price growth for Akurdi over the last 3 years\"",
      chartData: [],
      tableData: []
    }
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSend = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage = {
      type: 'user',
      text: input
    };

    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setIsLoading(true);

    try {
      const data = await queryAnalysis(userMessage.text);
      
      const botMessage = {
        type: 'bot',
        summary: data.summary,
        chartData: data.chart_data,
        tableData: data.table_data,
        areas: data.areas
      };
      
      setMessages(prev => [...prev, botMessage]);
    } catch (error) {
      const errorMessage = {
        type: 'bot',
        summary: "**Error**: I couldn't process your request. Please check if the backend server is running and try again.",
        chartData: [],
        tableData: []
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Container className="chat-container py-4">
      <div className="chat-history shadow-sm border">
        {messages.map((msg, index) => (
          <MessageDisplay key={index} message={msg} />
        ))}
        {isLoading && (
          <div className="message-bubble bot-message">
            <div className="loading-dots">Analyzing data</div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>
      
      <Form onSubmit={handleSend}>
        <InputGroup className="mb-3">
          <Form.Control
            placeholder="Ask about real estate trends..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            disabled={isLoading}
          />
          <Button 
            variant="primary" 
            type="submit" 
            disabled={isLoading || !input.trim()}
          >
            {isLoading ? <Spinner animation="border" size="sm" /> : 'Send'}
          </Button>
        </InputGroup>
      </Form>
    </Container>
  );
};

export default ChatInterface;
