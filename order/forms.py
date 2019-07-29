from django import forms
from django.forms import formset_factory, modelformset_factory
from django.forms import ModelForm
from .models import Order, Link, Screenshot, Shipping


class OrderModelForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['name', 'email', 'phone', 'address']
        labels = {
            'name': 'Name',
            'email': 'Email',
            'phone': 'Phone Number',
            'address':'Address'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full Name'
                }
            ),
            
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
                }
            ),

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number'
                }
            ),

            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full shipping address'
                }
            )
        }

# logged in user form
class OrderModelFormLoggedIn(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['address']
        labels = {
            'address':'Address'
        }
        widgets = {

            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your Full Address'
                }
            )
        }




LinkFormset = modelformset_factory(
    Link,
    fields=('link', ),
    extra=1,
    widgets={'link': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'link http://'
        })
    }
)



class ScreenShotForm(forms.ModelForm):
    
    class Meta:
        model = Screenshot
        fields = ('screenshot',)



ScreenShotFormset = modelformset_factory(Screenshot, form=ScreenShotForm, extra=1)



"""
ScreenShotFormset = modelformset_factory(
    Screenshot,
    fields=('screenshot', ),
    extra=1,
    widgets={'screenshot': forms.ClearableFileInput(attrs={
            'class': 'form-control'
    })
    }
)
"""

class ShippingForm(forms.ModelForm):
    
    class Meta:
        model = Shipping
        exclude = ('status', 'user')