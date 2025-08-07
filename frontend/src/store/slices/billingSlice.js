import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  invoices: [],
  payments: [],
  services: [],
  loading: false,
  error: null,
};

const billingSlice = createSlice({
  name: 'billing',
  initialState,
  reducers: {
    setLoading: (state, action) => {
      state.loading = action.payload;
    },
    setError: (state, action) => {
      state.error = action.payload;
    },
    clearError: (state) => {
      state.error = null;
    },
    setInvoices: (state, action) => {
      state.invoices = action.payload;
    },
    setPayments: (state, action) => {
      state.payments = action.payload;
    },
    setServices: (state, action) => {
      state.services = action.payload;
    },
    addInvoice: (state, action) => {
      state.invoices.push(action.payload);
    },
    updateInvoice: (state, action) => {
      const index = state.invoices.findIndex(i => i.id === action.payload.id);
      if (index !== -1) {
        state.invoices[index] = action.payload;
      }
    },
    deleteInvoice: (state, action) => {
      state.invoices = state.invoices.filter(i => i.id !== action.payload);
    },
  },
});

export const {
  setLoading,
  setError,
  clearError,
  setInvoices,
  setPayments,
  setServices,
  addInvoice,
  updateInvoice,
  deleteInvoice,
} = billingSlice.actions;

export default billingSlice.reducer;
