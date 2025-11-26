import React from 'react';
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
  BarChart,
  Bar
} from 'recharts';

const ChartComponent = ({ data, areas }) => {
  if (!data || data.length === 0) return null;

  // Determine if we should use Line or Bar chart based on data points
  // For single year comparison, Bar chart is better. For trends, Line chart.
  const isTrend = data.length > 1;

  // Generate random colors for different areas
  const colors = ['#8884d8', '#82ca9d', '#ffc658', '#ff7300', '#0088fe', '#00C49F'];

  return (
    <div className="chart-container" style={{ height: '400px', width: '100%' }}>
      <h5 className="mb-4 text-center">Real Estate Trends Analysis</h5>
      <ResponsiveContainer width="100%" height="100%">
        {isTrend ? (
          <LineChart
            data={data}
            margin={{ top: 5, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis />
            <Tooltip />
            <Legend />
            {areas.map((area, index) => (
              <React.Fragment key={area}>
                {/* Check if price data exists for this area */}
                {data[0][`${area}_price`] !== undefined && (
                  <Line
                    type="monotone"
                    dataKey={`${area}_price`}
                    name={`${area} Price`}
                    stroke={colors[index % colors.length]}
                    activeDot={{ r: 8 }}
                  />
                )}
                {/* Check if demand data exists for this area */}
                {data[0][`${area}_demand`] !== undefined && (
                  <Line
                    type="monotone"
                    dataKey={`${area}_demand`}
                    name={`${area} Demand`}
                    stroke={colors[(index + 3) % colors.length]}
                    strokeDasharray="5 5"
                  />
                )}
              </React.Fragment>
            ))}
          </LineChart>
        ) : (
          <BarChart
            data={data}
            margin={{ top: 5, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis />
            <Tooltip />
            <Legend />
            {areas.map((area, index) => (
              <React.Fragment key={area}>
                {data[0][`${area}_price`] !== undefined && (
                  <Bar dataKey={`${area}_price`} name={`${area} Price`} fill={colors[index % colors.length]} />
                )}
              </React.Fragment>
            ))}
          </BarChart>
        )}
      </ResponsiveContainer>
    </div>
  );
};

export default ChartComponent;
