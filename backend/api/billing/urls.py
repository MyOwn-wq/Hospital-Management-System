from django.urls import path
from . import views

app_name = 'billing'

urlpatterns = [
    # Service endpoints
    path('services/', views.ServiceListView.as_view(), name='service-list'),
    path('services/<int:pk>/', views.ServiceDetailView.as_view(), name='service-detail'),
    path('services/create/', views.ServiceCreateView.as_view(), name='service-create'),
    
    # Invoice endpoints
    path('invoices/', views.InvoiceListView.as_view(), name='invoice-list'),
    path('invoices/<int:pk>/', views.InvoiceDetailView.as_view(), name='invoice-detail'),
    path('invoices/create/', views.InvoiceCreateView.as_view(), name='invoice-create'),
    path('invoices/<int:pk>/update/', views.InvoiceUpdateView.as_view(), name='invoice-update'),
    path('invoices/<int:pk>/delete/', views.InvoiceDeleteView.as_view(), name='invoice-delete'),
    
    # Invoice item endpoints
    path('invoices/<int:invoice_pk>/items/', views.InvoiceItemListView.as_view(), name='invoice-item-list'),
    path('invoices/<int:invoice_pk>/items/<int:pk>/', views.InvoiceItemDetailView.as_view(), name='invoice-item-detail'),
    path('invoices/<int:invoice_pk>/items/create/', views.InvoiceItemCreateView.as_view(), name='invoice-item-create'),
    
    # Payment endpoints
    path('payments/', views.PaymentListView.as_view(), name='payment-list'),
    path('payments/<int:pk>/', views.PaymentDetailView.as_view(), name='payment-detail'),
    path('payments/create/', views.PaymentCreateView.as_view(), name='payment-create'),
    path('payments/<int:pk>/update/', views.PaymentUpdateView.as_view(), name='payment-update'),
]
