# Generated by Django 4.1.7 on 2023-05-18 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="School",
            fields=[
                (
                    "name",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("Principal", models.CharField(max_length=30)),
                ("Location", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                ("Sname", models.CharField(max_length=30)),
                ("Sage", models.IntegerField()),
                (
                    "school",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Student",
                        to="app.school",
                    ),
                ),
            ],
        ),
    ]
