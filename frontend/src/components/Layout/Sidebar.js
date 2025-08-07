import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { useSelector } from 'react-redux';
import {
  List,
  ListItem,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Divider,
} from '@mui/material';
import {
  Dashboard,
  People,
  LocalHospital,
  Event,
  Receipt,
  Folder,
  Person,
  AdminPanelSettings,
} from '@mui/icons-material';

const menuItems = [
  {
    text: 'Dashboard',
    icon: <Dashboard />,
    path: '/dashboard',
    roles: ['admin', 'doctor', 'receptionist', 'patient'],
  },
  {
    text: 'Patients',
    icon: <People />,
    path: '/patients',
    roles: ['admin', 'doctor', 'receptionist'],
  },
  {
    text: 'Doctors',
    icon: <LocalHospital />,
    path: '/doctors',
    roles: ['admin', 'receptionist'],
  },
  {
    text: 'Appointments',
    icon: <Event />,
    path: '/appointments',
    roles: ['admin', 'doctor', 'receptionist', 'patient'],
  },
  {
    text: 'Billing',
    icon: <Receipt />,
    path: '/billing',
    roles: ['admin', 'receptionist', 'patient'],
  },
  {
    text: 'Medical Records',
    icon: <Folder />,
    path: '/medical-records',
    roles: ['admin', 'doctor', 'receptionist', 'patient'],
  },
];

const Sidebar = ({ onItemClick }) => {
  const navigate = useNavigate();
  const location = useLocation();
  const { user } = useSelector((state) => state.auth);

  const handleItemClick = (path) => {
    navigate(path);
    if (onItemClick) {
      onItemClick();
    }
  };

  const filteredMenuItems = menuItems.filter(item =>
    item.roles.includes(user?.role || 'patient')
  );

  return (
    <List sx={{ pt: 1 }}>
      {filteredMenuItems.map((item, index) => (
        <ListItem key={item.text} disablePadding>
          <ListItemButton
            onClick={() => handleItemClick(item.path)}
            selected={location.pathname === item.path}
            sx={{
              mx: 1,
              borderRadius: 1,
              '&.Mui-selected': {
                backgroundColor: 'primary.main',
                color: 'white',
                '&:hover': {
                  backgroundColor: 'primary.dark',
                },
                '& .MuiListItemIcon-root': {
                  color: 'white',
                },
              },
              '&:hover': {
                backgroundColor: 'action.hover',
              },
            }}
          >
            <ListItemIcon
              sx={{
                color: location.pathname === item.path ? 'white' : 'inherit',
              }}
            >
              {item.icon}
            </ListItemIcon>
            <ListItemText primary={item.text} />
          </ListItemButton>
        </ListItem>
      ))}
      
      {user?.role === 'admin' && (
        <>
          <Divider sx={{ my: 2 }} />
          <ListItem disablePadding>
            <ListItemButton
              sx={{
                mx: 1,
                borderRadius: 1,
                '&:hover': {
                  backgroundColor: 'action.hover',
                },
              }}
            >
              <ListItemIcon>
                <AdminPanelSettings />
              </ListItemIcon>
              <ListItemText primary="Admin Panel" />
            </ListItemButton>
          </ListItem>
        </>
      )}
    </List>
  );
};

export default Sidebar;
