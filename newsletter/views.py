from django.contrib.auth import get_user_model
User = get_user_model()
from django.shortcuts import render, redirect, reverse
from django.http import request, HttpResponse, JsonResponse
from .models import Subscriber
from django.views.generic import CreateView, DetailView, UpdateView
from .forms import SubscriberForm, SubscriberUpdateForm


class Subcribing(CreateView):
    model = Subscriber
    form_class = SubscriberForm
    template_name = 'subscriber/subscriber_form.html'

    def get_success_url(self):
        return reverse('newsletter:subscribing', kwargs={'pk':self.object.pk})


class SubscriberDetail(DetailView):
    model = Subscriber
    template_name = 'subscriber/subscriber_detail.html'


class SubscriberUpdate(UpdateView):
    model = Subscriber
    form_class = SubscriberUpdateForm
    template_name = 'subscriber/subscriber_form.html'
    
    def get_success_url(self):
        return reverse('newsletter:subscribing', kwargs={'pk':self.object.pk})


def search_form(requet):
    return render(requet, 'subscriber/search_form.html')


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        subscriber = Subscriber.objects.filter(email__iexact=q)
        return render(request, 'subscriber/search_result.html',
                      {'subscriber': subscriber, 'query': q})
    else:
        return HttpResponse('enter your email address')



def subscribe(request):
    if 'email' in request.GET and request.GET['email']:
        email = request.GET['email']
        if Subscriber.objects.filter(email__iexact=email).exists():
            return HttpResponse('<h1>This email is already subscribed</h1>')
        else:
            subscriber = Subscriber(email=email)
            subscriber.save()
        return render(request, 'subscriber/thank.html')
    else:
        return HttpResponse('<h1>Go back and fill email correctly</h1>')

