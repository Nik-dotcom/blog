# Generated by Django 4.2.13 on 2024-05-08 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="contetnt",
            new_name="content",
        ),
    ]
