# Generated by Django 3.0.8 on 2020-08-05 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_trainer'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='trainer',
            field=models.ManyToManyField(related_name='Trainers', to='app.Trainer'),
        ),
    ]