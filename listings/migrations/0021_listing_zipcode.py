# Generated by Django 5.1.2 on 2024-10-14 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0020_remove_listing_zipcode_listing_maps_plan_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='zipcode',
            field=models.CharField(default='', max_length=20),
        ),
    ]
