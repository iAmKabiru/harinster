from django.contrib import admin
from .models import Newsletter, Subscriber

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email' ,'subscribed']
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['subject', 'date']

admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Subscriber, SubscriberAdmin)