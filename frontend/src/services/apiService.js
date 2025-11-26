import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

export const queryAnalysis = async (query) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/query/`, { query });
    return response.data;
  } catch (error) {
    console.error('Error querying analysis:', error);
    throw error;
  }
};

export const getAvailableAreas = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/areas/`);
    return response.data;
  } catch (error) {
    console.error('Error fetching areas:', error);
    throw error;
  }
};

export const healthCheck = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/health/`);
    return response.data;
  } catch (error) {
    console.error('Error checking health:', error);
    throw error;
  }
};
