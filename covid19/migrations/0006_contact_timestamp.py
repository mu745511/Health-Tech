# Generated by Django 3.0.8 on 2021-06-08 18:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('covid19', '0005_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
