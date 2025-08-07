from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    # Appointment endpoints
    path('', views.AppointmentListView.as_view(), name='appointment-list'),
    path('<int:pk>/', views.AppointmentDetailView.as_view(), name='appointment-detail'),
    path('create/', views.AppointmentCreateView.as_view(), name='appointment-create'),
    path('<int:pk>/update/', views.AppointmentUpdateView.as_view(), name='appointment-update'),
    path('<int:pk>/delete/', views.AppointmentDeleteView.as_view(), name='appointment-delete'),
    
    # Reminder endpoints
    path('<int:appointment_pk>/reminders/', views.AppointmentReminderListView.as_view(), name='reminder-list'),
    path('<int:appointment_pk>/reminders/<int:pk>/', views.AppointmentReminderDetailView.as_view(), name='reminder-detail'),
    path('<int:appointment_pk>/reminders/create/', views.AppointmentReminderCreateView.as_view(), name='reminder-create'),
    
    # Note endpoints
    path('<int:appointment_pk>/notes/', views.AppointmentNoteListView.as_view(), name='note-list'),
    path('<int:appointment_pk>/notes/<int:pk>/', views.AppointmentNoteDetailView.as_view(), name='note-detail'),
    path('<int:appointment_pk>/notes/create/', views.AppointmentNoteCreateView.as_view(), name='note-create'),
]
