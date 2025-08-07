import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  prescriptions: [],
  medicalDocuments: [],
  medicalNotes: [],
  loading: false,
  error: null,
};

const medicalRecordSlice = createSlice({
  name: 'medicalRecords',
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
    setPrescriptions: (state, action) => {
      state.prescriptions = action.payload;
    },
    setMedicalDocuments: (state, action) => {
      state.medicalDocuments = action.payload;
    },
    setMedicalNotes: (state, action) => {
      state.medicalNotes = action.payload;
    },
    addPrescription: (state, action) => {
      state.prescriptions.push(action.payload);
    },
    updatePrescription: (state, action) => {
      const index = state.prescriptions.findIndex(p => p.id === action.payload.id);
      if (index !== -1) {
        state.prescriptions[index] = action.payload;
      }
    },
    deletePrescription: (state, action) => {
      state.prescriptions = state.prescriptions.filter(p => p.id !== action.payload);
    },
  },
});

export const {
  setLoading,
  setError,
  clearError,
  setPrescriptions,
  setMedicalDocuments,
  setMedicalNotes,
  addPrescription,
  updatePrescription,
  deletePrescription,
} = medicalRecordSlice.actions;

export default medicalRecordSlice.reducer;
