# Generated by Django 4.2.3 on 2023-07-28 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("name", models.CharField(max_length=150)),
                ("lastname", models.CharField(max_length=150)),
                ("country", models.CharField(max_length=150)),
                ("email", models.EmailField(max_length=254)),
                ("still_alive", models.BooleanField()),
            ],
            options={
                "verbose_name": "author",
                "verbose_name_plural": "authors",
            },
        ),
    ]
