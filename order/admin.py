from django.utils.safestring import mark_safe
from django.contrib.admin import AdminSite
from django.contrib import admin
from django import forms
from django.forms import ModelForm
from .models import Order, Link, Store, Screenshot, Shipping



class ScreenhotAdmin(admin.ModelAdmin):
    list_per_page = 50
    readonly_fields = ['screenshot_image']
    list_display = ['screenshot', 'order']

    def screenshot_image(self, obj):
        return mark_safe('<img class="img img-fluid" src="{url}" width="{width}" height={height} />'.format(
            url = obj.screenshot.url,
            width=obj.screenshot.width,
            height=obj.screenshot.height,
            )
            )


class LinkAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ['link']
    list_display = ['link', 'order']

class ScreenshotInline(admin.StackedInline):
    list_per_page = 50
    model = Screenshot
    extra = 1
    readonly_fields = ['screenshot_image']

    def screenshot_image(self, obj):
        return mark_safe('<img class="img img-fluid" src="{url}" width="{width}" height={height} />'.format(
            url = obj.screenshot.url,
            width=obj.screenshot.width,
            height=obj.screenshot.height,
            )
            )
    

class LinkInline(admin.StackedInline):
    list_per_page = 50
    model = Link
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ['name','id', 'email', 'phone', 'address', 'date', 'status']
    search_fields = ['id', 'name', 'email', 'status']
    inlines = [LinkInline, ScreenshotInline]


class StoreAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ['name', 'url', 'logo']



# shipping
class ShippingForm(forms.ModelForm):

    class Meta:
        model = Shipping
        fields = ('name','email','phone','route','shipping_address', 'address', 'note', 'user', 'status')


class ShippingAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ['name','id', 'email', 'phone', 'route', 'date', 'status']
    search_fields = ['id', 'name', 'email', 'route', 'status']
    model = Shipping
    form = ShippingForm

admin.site.register(Order, OrderAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Screenshot, ScreenhotAdmin)
admin.site.register(Shipping, ShippingAdmin)