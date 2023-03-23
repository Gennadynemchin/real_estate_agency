# Generated by Django 2.2.24 on 2023-03-21 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("property", "0007_auto_20230321_1355"),
    ]

    operations = [
        migrations.CreateModel(
            name="Report",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField(verbose_name="Текст жалобы")),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор жалобы",
                    ),
                ),
                (
                    "flat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="property.Flat",
                        verbose_name="Объект",
                    ),
                ),
            ],
        ),
    ]
