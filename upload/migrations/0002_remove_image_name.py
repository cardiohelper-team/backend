# Generated by Django 4.0.4 on 2022-04-12 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='name',
        ),
    ]