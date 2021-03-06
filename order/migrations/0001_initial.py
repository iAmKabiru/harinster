# Generated by Django 2.2.7 on 2019-12-08 22:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(max_length=255, verbose_name='Delivery Address')),
                ('status', models.CharField(choices=[('recieved', 'recieved'), ('processing', 'processing'), ('completed', 'completed'), ('shipped', 'shipped'), ('delivered', 'delivered')], default='recieved', max_length=50)),
                ('date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField(max_length=1000)),
                ('logo', models.ImageField(upload_to='media/stores')),
            ],
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(choices=[('recieved', 'recieved'), ('processing', 'processing'), ('completed', 'completed'), ('shipped', 'shipped'), ('delivered', 'delivered')], default='recieved', max_length=50)),
                ('date', models.DateTimeField(auto_now=True)),
                ('shipping_address', models.CharField(max_length=1000, verbose_name='Shipping Address')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Delivery Address')),
                ('route', models.CharField(choices=[('UK to Nigeria', 'UK to Nigeria'), ('Nigeria to UK', 'Nigeria to UK')], max_length=255)),
                ('note', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'shipping',
                'verbose_name_plural': 'shipping',
            },
        ),
        migrations.CreateModel(
            name='Screenshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screenshot', models.ImageField(blank=True, upload_to='media/screenshots/%y/%m/%d')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='screenshots', to='order.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=1000, verbose_name='Source Link')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='links', to='order.Order')),
            ],
        ),
    ]
