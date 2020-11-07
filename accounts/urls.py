from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dashboard'),
    path('products/', views.products, name='products'),
    path('customer/<int:pk_test>/', views.customer, name='customer'),
]
