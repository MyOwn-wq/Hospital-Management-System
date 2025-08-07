import React from 'react';
import {
  Box,
  Grid,
  Card,
  CardContent,
  Typography,
  Paper,
  Avatar,
  List,
  ListItem,
  ListItemText,
  ListItemAvatar,
  Chip,
} from '@mui/material';
import {
  People,
  LocalHospital,
  Event,
  Receipt,
  TrendingUp,
  TrendingDown,
} from '@mui/icons-material';
import { useSelector } from 'react-redux';

const StatCard = ({ title, value, icon, color, trend }) => (
  <Card sx={{ height: '100%', position: 'relative', overflow: 'hidden' }}>
    <CardContent>
      <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
        <Avatar
          sx={{
            backgroundColor: color,
            width: 56,
            height: 56,
            mr: 2,
          }}
        >
          {icon}
        </Avatar>
        <Box sx={{ flexGrow: 1 }}>
          <Typography variant="h4" component="div" sx={{ fontWeight: 700 }}>
            {value}
          </Typography>
          <Typography variant="body2" color="text.secondary">
            {title}
          </Typography>
        </Box>
      </Box>
      {trend && (
        <Box sx={{ display: 'flex', alignItems: 'center' }}>
          {trend > 0 ? (
            <TrendingUp sx={{ color: 'success.main', fontSize: 16, mr: 0.5 }} />
          ) : (
            <TrendingDown sx={{ color: 'error.main', fontSize: 16, mr: 0.5 }} />
          )}
          <Typography
            variant="body2"
            color={trend > 0 ? 'success.main' : 'error.main'}
            sx={{ fontWeight: 600 }}
          >
            {Math.abs(trend)}% from last month
          </Typography>
        </Box>
      )}
    </CardContent>
  </Card>
);

const Dashboard = () => {
  const { user } = useSelector((state) => state.auth);

  // Mock data - in real app, this would come from API
  const stats = [
    {
      title: 'Total Patients',
      value: '1,234',
      icon: <People />,
      color: '#1976d2',
      trend: 12,
    },
    {
      title: 'Active Doctors',
      value: '45',
      icon: <LocalHospital />,
      color: '#2e7d32',
      trend: 5,
    },
    {
      title: 'Today\'s Appointments',
      value: '89',
      icon: <Event />,
      color: '#ed6c02',
      trend: -3,
    },
    {
      title: 'Monthly Revenue',
      value: '$45,678',
      icon: <Receipt />,
      color: '#9c27b0',
      trend: 18,
    },
  ];

  const recentAppointments = [
    {
      id: 1,
      patient: 'John Doe',
      doctor: 'Dr. Smith',
      time: '09:00 AM',
      status: 'confirmed',
    },
    {
      id: 2,
      patient: 'Jane Smith',
      doctor: 'Dr. Johnson',
      time: '10:30 AM',
      status: 'scheduled',
    },
    {
      id: 3,
      patient: 'Mike Wilson',
      doctor: 'Dr. Brown',
      time: '02:00 PM',
      status: 'completed',
    },
    {
      id: 4,
      patient: 'Sarah Davis',
      doctor: 'Dr. Wilson',
      time: '03:30 PM',
      status: 'confirmed',
    },
  ];

  const getStatusColor = (status) => {
    switch (status) {
      case 'confirmed':
        return 'success';
      case 'scheduled':
        return 'warning';
      case 'completed':
        return 'info';
      default:
        return 'default';
    }
  };

  return (
    <Box>
      <Typography variant="h4" component="h1" sx={{ mb: 3, fontWeight: 700 }}>
        Welcome back, {user?.first_name || user?.username}!
      </Typography>

      {/* Statistics Cards */}
      <Grid container spacing={3} sx={{ mb: 4 }}>
        {stats.map((stat, index) => (
          <Grid item xs={12} sm={6} md={3} key={index}>
            <StatCard {...stat} />
          </Grid>
        ))}
      </Grid>

      {/* Recent Appointments */}
      <Grid container spacing={3}>
        <Grid item xs={12} md={8}>
          <Paper sx={{ p: 3 }}>
            <Typography variant="h6" sx={{ mb: 2, fontWeight: 600 }}>
              Recent Appointments
            </Typography>
            <List>
              {recentAppointments.map((appointment) => (
                <ListItem
                  key={appointment.id}
                  sx={{
                    border: '1px solid',
                    borderColor: 'divider',
                    borderRadius: 1,
                    mb: 1,
                  }}
                >
                  <ListItemAvatar>
                    <Avatar sx={{ bgcolor: 'primary.main' }}>
                      {appointment.patient[0]}
                    </Avatar>
                  </ListItemAvatar>
                  <ListItemText
                    primary={appointment.patient}
                    secondary={`${appointment.doctor} • ${appointment.time}`}
                  />
                  <Chip
                    label={appointment.status}
                    color={getStatusColor(appointment.status)}
                    size="small"
                  />
                </ListItem>
              ))}
            </List>
          </Paper>
        </Grid>

        <Grid item xs={12} md={4}>
          <Paper sx={{ p: 3 }}>
            <Typography variant="h6" sx={{ mb: 2, fontWeight: 600 }}>
              Quick Actions
            </Typography>
            <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
              <Chip
                label="Add New Patient"
                color="primary"
                variant="outlined"
                clickable
                sx={{ justifyContent: 'flex-start', py: 1 }}
              />
              <Chip
                label="Schedule Appointment"
                color="secondary"
                variant="outlined"
                clickable
                sx={{ justifyContent: 'flex-start', py: 1 }}
              />
              <Chip
                label="Generate Report"
                color="info"
                variant="outlined"
                clickable
                sx={{ justifyContent: 'flex-start', py: 1 }}
              />
              <Chip
                label="View Billing"
                color="warning"
                variant="outlined"
                clickable
                sx={{ justifyContent: 'flex-start', py: 1 }}
              />
            </Box>
          </Paper>
        </Grid>
      </Grid>
    </Box>
  );
};

export default Dashboard;
