# Generated by Django 4.1.1 on 2022-09-22 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('engine', models.TextField(max_length=100)),
                ('hp', models.IntegerField(null=True)),
                ('nm', models.IntegerField(null=True)),
                ('KPP', models.CharField(choices=[('Mechanics', 'Mechanics'), ('Avomatick', 'Avomatick')], max_length=30)),
            ],
        ),
    ]
