from django.urls import path
from . import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'orders', views.OrderViewSet),
router.register(r'employee', views.EmployeeViewSet),
router.register(r'service', views.ServiceViewSet),
router.register(r'create', views.OrderCreateViewSet),



urlpatterns = [
    # path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('order', views.order, name='order'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.OrderDetailView.as_view(), name='order-detail'),
    path('<int:pk>/update', views.OrderUpdateView.as_view(), name='order-update'),
    path('<int:pk>/delete', views.OrderDeleteView.as_view(), name='order-delete'),
    path('employees', views.employees, name='employees'),
    path('services', views.services, name='services'),
    # path('orders/', views.OrderApiView.as_view(), name='api'),
    # path('orders/', views.snippet_list,),
    # path('orders/<int:pk>', views.OrderApiDetail.as_view()),
    # path('orders/<int:pk>', views.OrderApiDetail),
    # path('orders/create/', views.snippet_list_crate),
    # path('orders/create/<int:pk>', views.OrderApiDetail_crate),
    # path('employee/', views.employee_list),
    # path('employee/<int:pk>', views.EmployeeApiDetail),
    # path('service/', views.service_list),
    # path('service/<int:pk>', views.ServiceApiDetail),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]