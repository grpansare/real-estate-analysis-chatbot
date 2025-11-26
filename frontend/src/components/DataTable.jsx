import React from 'react';
import { Table } from 'react-bootstrap';

const DataTable = ({ data }) => {
  if (!data || data.length === 0) return null;

  return (
    <div className="data-table-container">
      <h5 className="mb-3">Detailed Data</h5>
      <Table striped bordered hover responsive size="sm">
        <thead>
          <tr>
            <th>Year</th>
            <th>Area</th>
            <th>Price/Sq.Ft</th>
            <th>Demand Score</th>
            <th>Avg Size (Sq.Ft)</th>
            <th>Transactions</th>
          </tr>
        </thead>
        <tbody>
          {data.map((row, index) => (
            <tr key={index}>
              <td>{row.Year}</td>
              <td>{row.Area}</td>
              <td>{row.Price_Per_SqFt}</td>
              <td>{row.Demand_Score}</td>
              <td>{row.Avg_Size_SqFt}</td>
              <td>{row.Transactions}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
};

export default DataTable;
