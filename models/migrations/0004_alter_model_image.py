# Generated by Django 4.1.1 on 2022-09-23 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0003_model_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]
