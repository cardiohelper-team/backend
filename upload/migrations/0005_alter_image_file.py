# Generated by Django 4.0.4 on 2022-04-27 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0004_alter_image_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.ImageField(upload_to='upload/media'),
        ),
    ]
