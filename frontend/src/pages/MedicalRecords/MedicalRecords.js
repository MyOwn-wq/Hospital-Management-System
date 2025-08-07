import React from 'react';
import { Box, Typography, Paper } from '@mui/material';

const MedicalRecords = () => {
  return (
    <Box sx={{ p: 3 }}>
      <Typography variant="h4" component="h1" sx={{ mb: 3 }}>
        Medical Records
      </Typography>
      <Paper sx={{ p: 3 }}>
        <Typography>Medical records management will be implemented here.</Typography>
      </Paper>
    </Box>
  );
};

export default MedicalRecords;
