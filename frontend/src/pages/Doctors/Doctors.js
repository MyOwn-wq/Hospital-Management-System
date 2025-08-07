import React from 'react';
import { Box, Typography, Paper } from '@mui/material';

const Doctors = () => {
  return (
    <Box sx={{ p: 3 }}>
      <Typography variant="h4" component="h1" sx={{ mb: 3 }}>
        Doctors
      </Typography>
      <Paper sx={{ p: 3 }}>
        <Typography>Doctor management will be implemented here.</Typography>
      </Paper>
    </Box>
  );
};

export default Doctors;
