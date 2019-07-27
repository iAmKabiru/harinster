from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20)

    def get_full_name(self):
        return self.first_name + " " + self.last_name

