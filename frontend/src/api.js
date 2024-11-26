import axios from 'axios';

const API_URL = 'http://localhost/api';

export const getHeroes = async () => {
  const response = await axios.get(`${API_URL}/heroes/`);
  return response.data;
};

export const createHero = async (hero) => {
  const response = await axios.post(`${API_URL}/heroes/`, hero);
  return response.data;
};

export const deleteHero = async (heroId) => {
  const response = await axios.delete(`${API_URL}/heroes/${heroId}`);
  return response.data;
};