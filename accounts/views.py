from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

from .forms import OrderForm, CustomerForm, ProductForm

# Create your views here.

def home(request):
    orders = Order.objects.all().order_by('-id')
    customers = Customer.objects.all().order_by('-id')

    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status = 'Pending').count()

    total_customers = customers.count()


    context = {
                'orders': orders,
                'customers': customers,
                'total_orders': total_orders,
                'delivered': delivered,
                'pending': pending,
            }
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()

    context = {'products': products}
    return render(request, 'accounts/products.html', context)

def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)

    orders = customer.order_set.all().order_by('-id')
    total_orders = orders.count()

    context = {
                'customer': customer,
                'orders': orders,
                'total_orders': total_orders,
            }
    return render(request, 'accounts/customer.html', context)

def createOrder(request):
    form = OrderForm()

    if request.method == 'POST':
        # print('Printing post: ', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)

def createCustomer(request):
    form = CustomerForm()

    if request.method == 'POST':
        # print('Printing post: ', request.POST)
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/customer_form.html', context)

def createProduct(request):
    form = ProductForm()

    if request.method == 'POST':
        # print('Printing post: ', request.POST)
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products/')

    context = {'form': form}
    return render(request, 'accounts/product_form.html', context)
