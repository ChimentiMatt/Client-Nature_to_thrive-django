# Generated by Django 3.2.7 on 2021-09-15 03:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('natureapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='event_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
