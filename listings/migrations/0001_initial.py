# Generated by Django 5.1.2 on 2024-10-10 21:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True)),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.DecimalField(decimal_places=1, max_digits=2)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(auto_now_add=True)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='listings/')),
                ('description', models.CharField(blank=True, max_length=200)),
                ('is_main', models.BooleanField(default=False)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='listings.listing')),
            ],
        ),
    ]
