from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail


class Subscriber(models.Model):
    email = models.EmailField()
    subscribed = models.BooleanField(default=True)

    def __str__(self):
        return self.email
  

subscribers = Subscriber.objects.filter(subscribed=True)
subscribers_list = []
for subscriber in subscribers:
    subscribers_list.append(subscriber.email)


class Newsletter(models.Model):
    subject = models.CharField(max_length=1000, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletter'

    def __str__(self):
        return self.subject
    

    def save(self, *args, **kwargs):
        if not self.pk:
            send_mail(self.subject, self.message, 'from@mail.com', subscribers_list, fail_silently=False)
            super().save(*args, **kwargs)
