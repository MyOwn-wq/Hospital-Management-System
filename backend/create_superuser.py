"""
Script to automatically create a superuser if one doesn't exist.
This can be run during deployment startup.
"""
import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

def create_superuser():
    """Create a superuser if one doesn't exist."""
    # Get credentials from environment variables or use defaults
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@hospital.com')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123')
    
    # Check if superuser already exists
    if User.objects.filter(username=username).exists():
        print(f'Superuser "{username}" already exists. Skipping creation.')
        return
    
    # Check if any superuser exists
    if User.objects.filter(is_superuser=True).exists():
        print('A superuser already exists. Skipping creation.')
        return
    
    # Create superuser
    try:
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print(f'Superuser "{username}" created successfully!')
        print(f'Username: {username}')
        print(f'Password: {password}')
        print('⚠️  IMPORTANT: Change this password after first login!')
    except Exception as e:
        print(f'Error creating superuser: {e}')
        sys.exit(1)

if __name__ == '__main__':
    create_superuser()

