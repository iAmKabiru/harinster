from django.urls import path, re_path
from . import views
from .views import create_order
from django.conf.urls import url

app_name = 'order'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('dashboard', views.dashboard, name = 'dashboard'),
    #path('create-order', views.OrderCreate.as_view(), name='create_order'),
    re_path(r'^order/create-order', create_order, name='create_order'),
    path('orders', views.OrderList.as_view(), name='order_list'),
    path('order-detail/<int:pk>', views.OrderDetail.as_view(), name='order_detail'),
    path('new-shipping', views.ShippingCreate.as_view(), name = 'shipping_create'),
    path('shippings', views.ShippingList.as_view(), name='shipping_list'),
    path('shipping-detail/<int:pk>', views.ShippingDetail.as_view(), name='shipping_detail'),
]
