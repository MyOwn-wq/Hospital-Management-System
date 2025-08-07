import React from 'react';
import { Box, Typography, Paper } from '@mui/material';

const Billing = () => {
  return (
    <Box sx={{ p: 3 }}>
      <Typography variant="h4" component="h1" sx={{ mb: 3 }}>
        Billing
      </Typography>
      <Paper sx={{ p: 3 }}>
        <Typography>Billing management will be implemented here.</Typography>
      </Paper>
    </Box>
  );
};

export default Billing;
