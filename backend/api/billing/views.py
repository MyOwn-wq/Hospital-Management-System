from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Service, Invoice, InvoiceItem, Payment
from .serializers import ServiceSerializer, InvoiceSerializer, InvoiceItemSerializer, PaymentSerializer


class ServiceListView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceCreateView(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class InvoiceListView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceCreateView(generics.CreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceUpdateView(generics.UpdateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceDeleteView(generics.DestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceItemListView(generics.ListCreateAPIView):
    serializer_class = InvoiceItemSerializer
    
    def get_queryset(self):
        return InvoiceItem.objects.filter(invoice_id=self.kwargs['invoice_pk'])


class InvoiceItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InvoiceItemSerializer
    
    def get_queryset(self):
        return InvoiceItem.objects.filter(invoice_id=self.kwargs['invoice_pk'])


class InvoiceItemCreateView(generics.CreateAPIView):
    serializer_class = InvoiceItemSerializer


class PaymentListView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentUpdateView(generics.UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
