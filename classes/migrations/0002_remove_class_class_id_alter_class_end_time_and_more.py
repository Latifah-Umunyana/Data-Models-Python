# Generated by Django 5.0.7 on 2024-07-18 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='class_id',
        ),
        migrations.AlterField(
            model_name='class',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='class',
            name='school_year',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='class',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
