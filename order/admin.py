from django.contrib import admin
from django import forms
from django.forms import ModelForm
from .models import Order, Link, Store, Screenshot, Shipping

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email', 'phone', 'address', 'date', 'status']
    search_fields = ['id', 'name', 'email']

class LinkAdmin(admin.ModelAdmin):
    list_display = ['link']

class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'logo']


# shipping
class ShippingForm(forms.ModelForm):

    class Meta:
        model = Shipping
        fields = ('name','email','phone','route','shipping_address', 'address', 'note', 'user', 'status')


class ShippingAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email', 'phone', 'route', 'date', 'status']
    model = Shipping
    form = ShippingForm

admin.site.register(Order, OrderAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Screenshot)
admin.site.register(Shipping, ShippingAdmin)