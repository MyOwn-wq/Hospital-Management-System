import api from './api';

const authService = {
  // Login user
  login: async (credentials) => {
    return api.post('/auth/login/', credentials);
  },

  // Register user
  register: async (userData) => {
    return api.post('/auth/register/', userData);
  },

  // Logout user
  logout: async () => {
    return api.post('/auth/logout/');
  },

  // Get user info
  getUserInfo: async () => {
    return api.get('/auth/user-info/');
  },

  // Update profile
  updateProfile: async (userData) => {
    return api.put('/auth/profile/', userData);
  },

  // Change password
  changePassword: async (passwordData) => {
    return api.put('/auth/change-password/', passwordData);
  },

  // Get token
  getToken: () => {
    return localStorage.getItem('token');
  },

  // Set token
  setToken: (token) => {
    localStorage.setItem('token', token);
  },

  // Remove token
  removeToken: () => {
    localStorage.removeItem('token');
  },

  // Check if user is authenticated
  isAuthenticated: () => {
    const token = localStorage.getItem('token');
    return !!token;
  },
};

export default authService;
