from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Prescription, Medication, MedicalDocument, MedicalNote
from .serializers import PrescriptionSerializer, MedicationSerializer, MedicalDocumentSerializer, MedicalNoteSerializer


class PrescriptionListView(generics.ListCreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer


class PrescriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer


class PrescriptionCreateView(generics.CreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer


class PrescriptionUpdateView(generics.UpdateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer


class PrescriptionDeleteView(generics.DestroyAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer


class MedicationListView(generics.ListCreateAPIView):
    serializer_class = MedicationSerializer
    
    def get_queryset(self):
        return Medication.objects.filter(prescription_id=self.kwargs['prescription_pk'])


class MedicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MedicationSerializer
    
    def get_queryset(self):
        return Medication.objects.filter(prescription_id=self.kwargs['prescription_pk'])


class MedicationCreateView(generics.CreateAPIView):
    serializer_class = MedicationSerializer


class MedicalDocumentListView(generics.ListCreateAPIView):
    queryset = MedicalDocument.objects.all()
    serializer_class = MedicalDocumentSerializer


class MedicalDocumentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalDocument.objects.all()
    serializer_class = MedicalDocumentSerializer


class MedicalDocumentCreateView(generics.CreateAPIView):
    queryset = MedicalDocument.objects.all()
    serializer_class = MedicalDocumentSerializer


class MedicalDocumentUpdateView(generics.UpdateAPIView):
    queryset = MedicalDocument.objects.all()
    serializer_class = MedicalDocumentSerializer


class MedicalDocumentDeleteView(generics.DestroyAPIView):
    queryset = MedicalDocument.objects.all()
    serializer_class = MedicalDocumentSerializer


class MedicalNoteListView(generics.ListCreateAPIView):
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializer


class MedicalNoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializer


class MedicalNoteCreateView(generics.CreateAPIView):
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializer


class MedicalNoteUpdateView(generics.UpdateAPIView):
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializer


class MedicalNoteDeleteView(generics.DestroyAPIView):
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializer
