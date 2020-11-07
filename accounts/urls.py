from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dashboard'),
    path('products/', views.products, name='products'),
    path('customer/<int:pk_test>/', views.customer, name='customer'),

    path('create_order/', views.createOrder, name='create_order'),
    path('update_order/<str:pk>', views.updateOrder, name='update_order'),

    path('create_customer/', views.createCustomer, name='create_customer'),

    path('create_product/', views.createProduct, name='create_product'),
]
