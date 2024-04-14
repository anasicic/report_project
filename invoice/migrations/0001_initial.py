# Generated by Django 4.2.11 on 2024-04-13 08:03

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CostCenter",
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
                ("cost_center_code", models.IntegerField()),
                ("cost_center_name", models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name="Supplier",
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
                ("supplier_name", models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name="TypeOfCost",
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
                ("cost_code", models.IntegerField()),
                ("cost_name", models.CharField(max_length=40)),
            ],
        ),
    ]
