"""harinster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from order.models import Order, Shipping, Store
from django.contrib.auth import get_user_model
User = get_user_model()


orders = Order.objects.all().count()
shippings = Shipping.objects.all().count()
stores = Store.objects.all().count()
users = User.objects.all().count()

urlpatterns = [
    path('admin/', admin.site.urls, {'extra_context' : {'orders': orders, 'shippings':shippings, 'stores':stores, 'users':users }}),
    #path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('order.urls')),
    path('', include('newsletter.urls')),
    path('/users/', include('django.contrib.auth.urls')),
    # pages urls
    path('howto', TemplateView.as_view(template_name='pages/howto.html'), name='howto'),
    path('about', TemplateView.as_view(template_name='pages/about.html'), name='about'),
    path('faq', TemplateView.as_view(template_name='pages/faq.html'), name='faq'),
    path('contact', TemplateView.as_view(template_name='pages/contact.html'), name='contact'),
    path('customer-service', TemplateView.as_view(template_name='pages/customer_service.html'), name='customer_service'),
    path('terms-and-conditions', TemplateView.as_view(template_name='pages/terms.html'), name='terms'),
    path('privacy-policy', TemplateView.as_view(template_name='pages/privacy_policy.html'), name='privacy_policy'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Harinster"
admin.site.site_title = "Harinster"
admin.site.index_title = "Harinster"