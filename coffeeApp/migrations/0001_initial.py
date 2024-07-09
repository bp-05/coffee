# Generated by Django 5.0.6 on 2024-07-03 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoffeeForm',
            fields=[
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('tipo_solicitud', models.CharField(max_length=50)),
                ('mensaje', models.CharField(max_length=200)),
            ],
        ),
    ]
