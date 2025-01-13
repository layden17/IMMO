import axios from 'axios';

const API_URL = 'http://localhost:5001/api/customers';

export const fetchCustomers = async () => {
  const response = await axios.get(API_URL);
  return response.data;
};

export const createCustomer = async (customerData) => {
  const response = await axios.post(API_URL, customerData);
  return response.data;
};
