from django.urls import path
from . import views


app_name = 'newsletter'

urlpatterns = [
    path('subscribe', views.subscribe, name='subscribe'),
    path('subscribe_', views.Subcribing.as_view(), name='subscribe_'),
    path('subscribing-detail/<int:pk>/', views.SubscriberDetail.as_view(), name='subscribing'),
    path('search-form', views.search_form, name = 'search_email'),
    path('search', views.search, name='search'),
    path('update-subscription/<int:pk>/', views.SubscriberUpdate.as_view(), name = 'update_subscription'),
]
