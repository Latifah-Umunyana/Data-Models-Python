# Generated by Django 5.0.7 on 2024-10-18 14:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("course", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Teacher",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                (
                    "date_of_birth",
                    models.DateField(default=datetime.date.today, verbose_name="Date"),
                ),
                ("country", models.CharField(max_length=28)),
                ("gender", models.CharField(max_length=6)),
                ("Bio", models.TextField()),
                ("courses", models.ManyToManyField(to="course.course")),
            ],
        ),
    ]
