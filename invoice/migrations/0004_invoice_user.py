# Generated by Django 4.2.11 on 2024-04-28 15:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("invoice", "0003_rename_cost_center_invoice_cost_center_code_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoice",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
