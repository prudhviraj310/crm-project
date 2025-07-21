import axios from './axios';

export const registerUser = async (userData) => {
    const response = await axios.post('/users/register', userData);
    return response.data;
};

export const loginUser = async (userData) => {
    const response = await axios.post('/users/login', userData);
    return response.data;
};
