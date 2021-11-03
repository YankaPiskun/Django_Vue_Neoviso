from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Order, Car, Service, Employee
from .forms import OrderForm
from django.views.generic import DetailView, UpdateView, DeleteView
from .serializers import OrderSerializer, OrderCrateSerializer, CarSerializer, EmployeeSerializer, ServiceSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import viewsets, permissions




# Create your views here.

def frontend(request):
  return HttpResponse(render(request, 'vue_index.html'))

def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница!!'})


def about(request):
    return render(request, 'main/about.html')


def employees(request):
    return render(request, 'main/employees.html')


def services(request):
    return render(request, 'main/services.html')


def order(request):
    orders = Order.objects.all()
    return render(request, "main/order.html", {'title': 'Заказы', 'orders': orders})


def create(request):
    error = ''
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order')
        else:
            error = 'Форма была не верной'

    form = OrderForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', data)


class OrderDetailView(DetailView):
    model = Order
    template_name = 'main/details_view.html'
    context_object_name = 'order'


class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'main/create.html'

    form_class = OrderForm


class OrderDeleteView(DeleteView):
    model = Order
    success_url = '/order'
    template_name = 'main/order-delete.html'



class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderCreateViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderCrateSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer






