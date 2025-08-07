import React from 'react';
import { Box, Typography, Paper } from '@mui/material';

const Appointments = () => {
  return (
    <Box sx={{ p: 3 }}>
      <Typography variant="h4" component="h1" sx={{ mb: 3 }}>
        Appointments
      </Typography>
      <Paper sx={{ p: 3 }}>
        <Typography>Appointment management will be implemented here.</Typography>
      </Paper>
    </Box>
  );
};

export default Appointments;
