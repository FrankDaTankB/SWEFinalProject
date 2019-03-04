from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='verso-home'),
    path('index/', views.index, name='verso-index'),
    path('customerReg/', views.customerReg, name='verso-customerReg'),
    path('searchCustomer/', views.searchCustomer, name='verso-searchCustomer')
]
