# Generated by Django 3.0.5 on 2020-07-19 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200703_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='sector',
            field=models.CharField(blank=True, choices=[('NGO', 'NON Goverment Orgarnization'), ('IO', 'International Organization'), ('NG', 'National Government'), ('PS', 'Private Sector'), ('RO', 'Regional Organization'), ('O', 'Others')], max_length=100, null=True),
        ),
    ]