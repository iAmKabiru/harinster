from django.contrib.auth import get_user_model
User = get_user_model()
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from .forms import OrderModelForm, LinkFormset, ScreenShotFormset, ShippingForm, OrderModelFormLoggedIn
from .models import Store, Order, Link, Screenshot, Shipping
from django.http import HttpResponseRedirect


user = User.objects.all()

@login_required
def dashboard(request):
    context = {}
    context['orders'] = Order.objects.filter(user=request.user).count()
    context['shippings'] = Shipping.objects.filter(user=request.user).count()
    return render(request, 'dashboard.html', context)


class HomeView(ListView):
    model = Store
    template_name = 'home.html'


def create_order(request):
    template_name = 'order/order_form.html'
    
    if request.method == 'GET':
        orderform = OrderModelForm(request.GET or None)
        formset = LinkFormset(queryset = Link.objects.none())
        picset = ScreenShotFormset(queryset = Screenshot.objects.none())
    
    elif request.method == 'POST':
        orderform = OrderModelForm(request.POST, request.FILES)
        formset = LinkFormset(request.POST)
        picset = ScreenShotFormset(request.POST, request.FILES, queryset=Screenshot.objects.none())
        if orderform.is_valid() and formset.is_valid() and picset.is_valid():
            if request.user.is_authenticated:
                order = orderform.save(commit=False)
                order.name = request.user.get_full_name()
                order.email = request.user.email
                order.phone = request.user.phone
                order.user = request.user
                order.save()
            else:
                order = orderform.save()
            
            for form in picset:
                screenshot = form.save(commit=False)
                screenshot.order = order
                screenshot.save()
            for form in formset:
                link = form.save(commit=False)
                link.order = order
                link.save()
           
            return HttpResponseRedirect("/order-detail/{id}".format(id= order.id))

    else:
        orderform = OrderModelForm(request.POST)
        formset = LinkFormset(request.POST)
        picset = ScreenShotFormset(request.POST, request.FILES)    
    return render(request, template_name, {
        'orderform': orderform,
        'formset': formset,
        'picset': picset,
        })


class OrderList(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order/order_list.html'

    def get_queryset(self):
        qs = Order.objects.filter(user=self.request.user)
        return qs
    
class OrderDetail(DetailView):
    model = Order



def create_shipping(request):
    template_name = 'shipping/shipping_form.html'

    if request.method == 'POST':
        form = ShippingForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                shipping = form.save(commit=False)
                shipping.name = request.user.get_full_name()
                shipping.email = request.user.email
                shipping.phone = request.user.phone
                shipping.user = request.user
                form.save()
            else:
                shipping = form.save()
            return redirect('order:shipping_detail', pk=shipping.pk)
    else:
        form = ShippingForm()
    return render(request, template_name, context={'form':form})



"""
class ShippingCreate(CreateView):
    model = Shipping
    form_class = ShippingForm
    template_name = 'shipping/shipping_form.html'

    def get_success_url(self):
        return reverse('order:shipping_detail', kwargs={'pk':self.object.pk})
"""

class ShippingList(LoginRequiredMixin, ListView):
    model = Shipping
    template_name = 'shipping/shipping_list.html'

    def get_queryset(self):
        qs = Shipping.objects.filter(user=self.request.user)
        return qs

class ShippingDetail(DetailView):
    model = Shipping
    template_name = 'shipping/shipping_detail.html'