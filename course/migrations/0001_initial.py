# Generated by Django 5.0.7 on 2024-08-19 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.IntegerField()),
                ('course_name', models.CharField(max_length=20)),
                ('department_id', models.IntegerField()),
                ('instructor_id', models.IntegerField()),
                ('enrollment_capacity', models.PositiveSmallIntegerField()),
                ('location', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=15)),
            ],
        ),
    ]
