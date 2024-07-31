# Generated by Django 5.0.7 on 2024-07-31 13:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NetworkElement",
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
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("country", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                ("street", models.CharField(max_length=100)),
                ("house_number", models.CharField(max_length=10)),
                ("product_name", models.CharField(max_length=255)),
                ("product_model", models.CharField(max_length=255)),
                ("product_release_date", models.DateField()),
                ("debt", models.DecimalField(decimal_places=2, max_digits=10)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "supplier",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="clients",
                        to="network.networkelement",
                    ),
                ),
            ],
        ),
    ]
