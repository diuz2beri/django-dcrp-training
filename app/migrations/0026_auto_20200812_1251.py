# Generated by Django 3.0.8 on 2020-08-12 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20200811_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='phone_contact',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]