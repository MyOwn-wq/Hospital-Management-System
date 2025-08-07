from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Doctor, Specialization, DoctorAvailability, DoctorLeave
from .serializers import DoctorSerializer, SpecializationSerializer, DoctorAvailabilitySerializer, DoctorLeaveSerializer


class DoctorListView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorCreateView(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorUpdateView(generics.UpdateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorDeleteView(generics.DestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class SpecializationListView(generics.ListCreateAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class SpecializationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class DoctorAvailabilityListView(generics.ListCreateAPIView):
    serializer_class = DoctorAvailabilitySerializer
    
    def get_queryset(self):
        return DoctorAvailability.objects.filter(doctor_id=self.kwargs['doctor_pk'])


class DoctorAvailabilityDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorAvailabilitySerializer
    
    def get_queryset(self):
        return DoctorAvailability.objects.filter(doctor_id=self.kwargs['doctor_pk'])


class DoctorAvailabilityCreateView(generics.CreateAPIView):
    serializer_class = DoctorAvailabilitySerializer


class DoctorLeaveListView(generics.ListCreateAPIView):
    serializer_class = DoctorLeaveSerializer
    
    def get_queryset(self):
        return DoctorLeave.objects.filter(doctor_id=self.kwargs['doctor_pk'])


class DoctorLeaveDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorLeaveSerializer
    
    def get_queryset(self):
        return DoctorLeave.objects.filter(doctor_id=self.kwargs['doctor_pk'])


class DoctorLeaveCreateView(generics.CreateAPIView):
    serializer_class = DoctorLeaveSerializer
