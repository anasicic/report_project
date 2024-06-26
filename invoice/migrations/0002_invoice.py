# Generated by Django 4.2.11 on 2024-04-27 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("invoice", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Invoice",
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
                ("netto_amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date", models.DateField()),
                ("invoice_number", models.CharField(max_length=20)),
                (
                    "cost_center",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="invoice.costcenter",
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="invoice.supplier",
                    ),
                ),
                (
                    "type_of_cost",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="invoice.typeofcost",
                    ),
                ),
            ],
        ),
    ]
