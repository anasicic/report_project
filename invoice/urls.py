from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='invoice-home'),
    path('create/', views.create_invoice, name='create-invoice'),
    path('detail/<int:pk>/', views.invoice_detail, name='invoice-detail'),
    path('delete_invoice/<int:pk>/', views.delete_invoice, name='delete_invoice'),
    path('delete_invoice_detail/<int:pk>/', views.delete_invoice_detail, name='delete_invoice_detail'),
    path('update_invoice/<int:pk>/', views.update_invoice, name='update_invoice'),
]