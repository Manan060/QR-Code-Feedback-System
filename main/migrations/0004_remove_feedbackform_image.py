# Generated by Django 4.1.2 on 2023-03-31 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_profile"),
    ]

    operations = [
        migrations.RemoveField(model_name="feedbackform", name="image",),
    ]
