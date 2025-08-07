from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Appointment, AppointmentReminder, AppointmentNote
from .serializers import AppointmentSerializer, AppointmentReminderSerializer, AppointmentNoteSerializer


class AppointmentListView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentCreateView(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentUpdateView(generics.UpdateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentDeleteView(generics.DestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentReminderListView(generics.ListCreateAPIView):
    serializer_class = AppointmentReminderSerializer
    
    def get_queryset(self):
        return AppointmentReminder.objects.filter(appointment_id=self.kwargs['appointment_pk'])


class AppointmentReminderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppointmentReminderSerializer
    
    def get_queryset(self):
        return AppointmentReminder.objects.filter(appointment_id=self.kwargs['appointment_pk'])


class AppointmentReminderCreateView(generics.CreateAPIView):
    serializer_class = AppointmentReminderSerializer


class AppointmentNoteListView(generics.ListCreateAPIView):
    serializer_class = AppointmentNoteSerializer
    
    def get_queryset(self):
        return AppointmentNote.objects.filter(appointment_id=self.kwargs['appointment_pk'])


class AppointmentNoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppointmentNoteSerializer
    
    def get_queryset(self):
        return AppointmentNote.objects.filter(appointment_id=self.kwargs['appointment_pk'])


class AppointmentNoteCreateView(generics.CreateAPIView):
    serializer_class = AppointmentNoteSerializer
