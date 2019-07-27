from django.db import models
from users.models import CustomUser

class Order(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, verbose_name = "Delivery Address")
    user = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.CASCADE)

    status_choices = (
        ('recieved','recieved'),
        ('processing', 'processing'),
        ('completed', 'completed'),
        ('shipped', 'shipped'),
        ('delivered', 'delivered')
    )
    status = models.CharField(max_length=50, choices = status_choices, default='recieved')
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "order"+ " " + str(self.id)
    """    
    def save(self, *args, **kwargs):
        if not.slf.pk:
    """

    def get_absolute_url(self):
        return reverse("order_detail", kwargs={"pk": self.pk})

    class Meta:
        ordering= ['-date']
            


class Link(models.Model):
    link = models.URLField(max_length=1000, verbose_name = "Source Link")
    order = models.ForeignKey(Order, blank=True, null=True, on_delete=models.CASCADE, related_name="links")

class Screenshot(models.Model):
    screenshot = models.ImageField(upload_to='media/screenshots/%y/%m/%d', blank = True)
    order = models.ForeignKey(Order, blank=True, null=True, on_delete=models.CASCADE, related_name="screenshots")


class Shipping(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.CASCADE)

    status_choices = (
        ('recieved','recieved'),
        ('processing', 'processing'),
        ('completed', 'completed'),
        ('shipped', 'shipped'),
        ('delivered', 'delivered')
    )
    status = models.CharField(max_length=50, choices = status_choices, default='recieved')
    date = models.DateTimeField(auto_now=True)
    route_choices = (
        ('UK to Nigeria', 'UK to Nigeria'),
        ('Nigeria to UK', 'Nigeria to UK')
    )
    shipping_address = models.CharField(max_length=1000, verbose_name = 'Shipping Address')
    address = models.CharField(max_length=255, verbose_name = "Delivery Address", blank=True, null=True)
    route = models.CharField(max_length=255, choices = route_choices)
    note = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'shipping'
        verbose_name_plural = 'shipping'

    def __str__(self):
        return str(self.id)
    

class Store(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=1000)
    logo = models.ImageField(upload_to='media/stores', blank=False)

    def __str__(self):
        return self.name