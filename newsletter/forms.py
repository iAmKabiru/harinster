from django import forms
from django.forms import ModelForm
from .models import Subscriber


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']

class SubscriberUpdateForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['subscribed']