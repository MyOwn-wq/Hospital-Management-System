from django.urls import path
from . import views

app_name = 'doctors'

urlpatterns = [
    # Doctor endpoints
    path('', views.DoctorListView.as_view(), name='doctor-list'),
    path('<int:pk>/', views.DoctorDetailView.as_view(), name='doctor-detail'),
    path('create/', views.DoctorCreateView.as_view(), name='doctor-create'),
    path('<int:pk>/update/', views.DoctorUpdateView.as_view(), name='doctor-update'),
    path('<int:pk>/delete/', views.DoctorDeleteView.as_view(), name='doctor-delete'),
    
    # Specialization endpoints
    path('specializations/', views.SpecializationListView.as_view(), name='specialization-list'),
    path('specializations/<int:pk>/', views.SpecializationDetailView.as_view(), name='specialization-detail'),
    
    # Availability endpoints
    path('<int:doctor_pk>/availability/', views.DoctorAvailabilityListView.as_view(), name='availability-list'),
    path('<int:doctor_pk>/availability/<int:pk>/', views.DoctorAvailabilityDetailView.as_view(), name='availability-detail'),
    path('<int:doctor_pk>/availability/create/', views.DoctorAvailabilityCreateView.as_view(), name='availability-create'),
    
    # Leave endpoints
    path('<int:doctor_pk>/leaves/', views.DoctorLeaveListView.as_view(), name='leave-list'),
    path('<int:doctor_pk>/leaves/<int:pk>/', views.DoctorLeaveDetailView.as_view(), name='leave-detail'),
    path('<int:doctor_pk>/leaves/create/', views.DoctorLeaveCreateView.as_view(), name='leave-create'),
]
