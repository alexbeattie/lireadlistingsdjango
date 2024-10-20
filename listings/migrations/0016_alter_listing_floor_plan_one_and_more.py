# Generated by Django 5.1.2 on 2024-10-11 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0015_listing_floor_plan_one_listing_floor_plan_two_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='floor_plan_one',
            field=models.FileField(blank=True, null=True, upload_to='listings/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='floor_plan_two',
            field=models.FileField(blank=True, null=True, upload_to='listings/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='maps_plan',
            field=models.FileField(blank=True, null=True, upload_to='listings/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='listings/'),
        ),
    ]
