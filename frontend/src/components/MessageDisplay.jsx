import React from 'react';
import ReactMarkdown from 'react-markdown';
import ChartComponent from './ChartComponent';
import DataTable from './DataTable';

const MessageDisplay = ({ message }) => {
  const isUser = message.type === 'user';
  
  return (
    <div className={`message-bubble ${isUser ? 'user-message' : 'bot-message'}`}>
      {isUser ? (
        <div className="message-content">
          {message.text}
        </div>
      ) : (
        <div className="message-content">
          {/* Summary Text */}
          <div className="mb-3">
            <ReactMarkdown>{message.summary}</ReactMarkdown>
          </div>
          
          {/* Chart Visualization */}
          {message.chartData && message.chartData.length > 0 && (
            <ChartComponent 
              data={message.chartData} 
              areas={message.areas || []} 
            />
          )}
          
          {/* Data Table */}
          {message.tableData && message.tableData.length > 0 && (
            <DataTable data={message.tableData} />
          )}
        </div>
      )}
    </div>
  );
};

export default MessageDisplay;
