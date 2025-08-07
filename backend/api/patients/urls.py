from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    # Patient endpoints
    path('', views.PatientListView.as_view(), name='patient-list'),
    path('<int:pk>/', views.PatientDetailView.as_view(), name='patient-detail'),
    path('create/', views.PatientCreateView.as_view(), name='patient-create'),
    path('<int:pk>/update/', views.PatientUpdateView.as_view(), name='patient-update'),
    path('<int:pk>/delete/', views.PatientDeleteView.as_view(), name='patient-delete'),
    
    # Medical history endpoints
    path('<int:patient_pk>/medical-history/', views.MedicalHistoryListView.as_view(), name='medical-history-list'),
    path('<int:patient_pk>/medical-history/<int:pk>/', views.MedicalHistoryDetailView.as_view(), name='medical-history-detail'),
    path('<int:patient_pk>/medical-history/create/', views.MedicalHistoryCreateView.as_view(), name='medical-history-create'),
    
    # Lab report endpoints
    path('<int:patient_pk>/lab-reports/', views.LabReportListView.as_view(), name='lab-report-list'),
    path('<int:patient_pk>/lab-reports/<int:pk>/', views.LabReportDetailView.as_view(), name='lab-report-detail'),
    path('<int:patient_pk>/lab-reports/create/', views.LabReportCreateView.as_view(), name='lab-report-create'),
]
