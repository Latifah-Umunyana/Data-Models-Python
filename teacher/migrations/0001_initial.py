# Generated by Django 3.2.12 on 2024-06-17 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=28)),
                ('id_number', models.IntegerField()),
                ('gender', models.CharField(max_length=6)),
                ('Bio', models.TextField()),
            ],
        ),
    ]
