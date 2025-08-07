import React from 'react';
import { Box, Typography, Paper } from '@mui/material';

const Profile = () => {
  return (
    <Box sx={{ p: 3 }}>
      <Typography variant="h4" component="h1" sx={{ mb: 3 }}>
        Profile
      </Typography>
      <Paper sx={{ p: 3 }}>
        <Typography>User profile management will be implemented here.</Typography>
      </Paper>
    </Box>
  );
};

export default Profile;
