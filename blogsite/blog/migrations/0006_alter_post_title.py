# Generated by Django 4.2.13 on 2024-05-09 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_alter_post_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=100, verbose_name="Заголовок записи"),
        ),
    ]