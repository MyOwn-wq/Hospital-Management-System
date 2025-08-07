"""
URL configuration for hospital project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


def home(request):
    """Welcome page for the Hospital Management System API"""
    return JsonResponse({
        "message": "Welcome to the Hospital Management System API!",
        "version": "1.0.0",
        "description": "A comprehensive healthcare management system",
        "endpoints": {
            "admin": "/admin/",
            "authentication": "/api/auth/",
            "patients": "/api/patients/",
            "doctors": "/api/doctors/",
            "appointments": "/api/appointments/",
            "billing": "/api/billing/",
            "medical_records": "/api/medical-records/"
        },
        "documentation": "Check the README.md file for detailed API documentation"
    })

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('admin/', admin.site.urls),
    
    # JWT Authentication
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # API endpoints
    path('api/auth/', include('api.authentication.urls')),
    path('api/patients/', include('api.patients.urls')),
    path('api/doctors/', include('api.doctors.urls')),
    path('api/appointments/', include('api.appointments.urls')),
    path('api/billing/', include('api.billing.urls')),
    path('api/medical-records/', include('api.medical_records.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
