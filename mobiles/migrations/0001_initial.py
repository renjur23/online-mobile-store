# Generated by Django 5.0.1 on 2024-01-21 07:06

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Mobile",
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
                ("name", models.CharField(max_length=200)),
                ("manufacturer", models.CharField(max_length=200)),
                ("description", models.CharField(default=None, max_length=500)),
                ("price", models.FloatField(blank=True, null=True)),
                ("image_url", models.CharField(default=False, max_length=2083)),
                ("mobile_available", models.BooleanField(default=False)),
            ],
        ),
    ]