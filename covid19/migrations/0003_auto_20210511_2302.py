# Generated by Django 3.0.8 on 2021-05-11 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid19', '0002_auto_20210408_2339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Covid_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]
