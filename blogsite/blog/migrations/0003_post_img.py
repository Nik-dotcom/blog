# Generated by Django 4.2.13 on 2024-05-08 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_rename_contetnt_post_content"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="img",
            field=models.ImageField(
                default="img.jpeg", upload_to="image/%Y", verbose_name="Изображение"
            ),
            preserve_default=False,
        ),
    ]
