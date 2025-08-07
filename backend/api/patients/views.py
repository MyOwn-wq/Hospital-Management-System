from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Patient, MedicalHistory, LabReport
from .serializers import PatientSerializer, MedicalHistorySerializer, LabReportSerializer


class PatientListView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientCreateView(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientUpdateView(generics.UpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientDeleteView(generics.DestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class MedicalHistoryListView(generics.ListCreateAPIView):
    serializer_class = MedicalHistorySerializer
    
    def get_queryset(self):
        return MedicalHistory.objects.filter(patient_id=self.kwargs['patient_pk'])


class MedicalHistoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MedicalHistorySerializer
    
    def get_queryset(self):
        return MedicalHistory.objects.filter(patient_id=self.kwargs['patient_pk'])


class MedicalHistoryCreateView(generics.CreateAPIView):
    serializer_class = MedicalHistorySerializer


class LabReportListView(generics.ListCreateAPIView):
    serializer_class = LabReportSerializer
    
    def get_queryset(self):
        return LabReport.objects.filter(patient_id=self.kwargs['patient_pk'])


class LabReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LabReportSerializer
    
    def get_queryset(self):
        return LabReport.objects.filter(patient_id=self.kwargs['patient_pk'])


class LabReportCreateView(generics.CreateAPIView):
    serializer_class = LabReportSerializer
