import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  doctors: [],
  specializations: [],
  loading: false,
  error: null,
};

const doctorSlice = createSlice({
  name: 'doctors',
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
    setDoctors: (state, action) => {
      state.doctors = action.payload;
    },
    setSpecializations: (state, action) => {
      state.specializations = action.payload;
    },
    addDoctor: (state, action) => {
      state.doctors.push(action.payload);
    },
    updateDoctor: (state, action) => {
      const index = state.doctors.findIndex(d => d.id === action.payload.id);
      if (index !== -1) {
        state.doctors[index] = action.payload;
      }
    },
    deleteDoctor: (state, action) => {
      state.doctors = state.doctors.filter(d => d.id !== action.payload);
    },
  },
});

export const {
  setLoading,
  setError,
  clearError,
  setDoctors,
  setSpecializations,
  addDoctor,
  updateDoctor,
  deleteDoctor,
} = doctorSlice.actions;

export default doctorSlice.reducer;
