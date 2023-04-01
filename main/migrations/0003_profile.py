# Generated by Django 4.1.2 on 2023-03-28 16:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_rename_imgage_feedbackform_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("username", models.CharField(max_length=40)),
                ("phone_number", models.CharField(max_length=13)),
                ("otp", models.CharField(blank=True, max_length=100, null=True)),
                ("uid", models.UUIDField(default=uuid.uuid4)),
            ],
        ),
    ]