from django.urls import path
from . import views

app_name = 'medical_records'

urlpatterns = [
    # Prescription endpoints
    path('prescriptions/', views.PrescriptionListView.as_view(), name='prescription-list'),
    path('prescriptions/<int:pk>/', views.PrescriptionDetailView.as_view(), name='prescription-detail'),
    path('prescriptions/create/', views.PrescriptionCreateView.as_view(), name='prescription-create'),
    path('prescriptions/<int:pk>/update/', views.PrescriptionUpdateView.as_view(), name='prescription-update'),
    path('prescriptions/<int:pk>/delete/', views.PrescriptionDeleteView.as_view(), name='prescription-delete'),
    
    # Medication endpoints
    path('prescriptions/<int:prescription_pk>/medications/', views.MedicationListView.as_view(), name='medication-list'),
    path('prescriptions/<int:prescription_pk>/medications/<int:pk>/', views.MedicationDetailView.as_view(), name='medication-detail'),
    path('prescriptions/<int:prescription_pk>/medications/create/', views.MedicationCreateView.as_view(), name='medication-create'),
    
    # Medical document endpoints
    path('documents/', views.MedicalDocumentListView.as_view(), name='document-list'),
    path('documents/<int:pk>/', views.MedicalDocumentDetailView.as_view(), name='document-detail'),
    path('documents/create/', views.MedicalDocumentCreateView.as_view(), name='document-create'),
    path('documents/<int:pk>/update/', views.MedicalDocumentUpdateView.as_view(), name='document-update'),
    path('documents/<int:pk>/delete/', views.MedicalDocumentDeleteView.as_view(), name='document-delete'),
    
    # Medical note endpoints
    path('notes/', views.MedicalNoteListView.as_view(), name='note-list'),
    path('notes/<int:pk>/', views.MedicalNoteDetailView.as_view(), name='note-detail'),
    path('notes/create/', views.MedicalNoteCreateView.as_view(), name='note-create'),
    path('notes/<int:pk>/update/', views.MedicalNoteUpdateView.as_view(), name='note-update'),
    path('notes/<int:pk>/delete/', views.MedicalNoteDeleteView.as_view(), name='note-delete'),
]
