# Generated by Django 4.1.2 on 2023-03-28 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="feedbackform", old_name="imgage", new_name="image",
        ),
    ]
