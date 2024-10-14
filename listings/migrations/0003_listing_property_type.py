# Generated by Django 5.1.2 on 2024-10-10 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_alter_listing_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='property_type',
            field=models.CharField(choices=[('house', 'House'), ('apartment', 'Apartment'), ('condo', 'Condo'), ('townhouse', 'Townhouse'), ('land', 'Land')], default='land', max_length=20),
        ),
    ]
