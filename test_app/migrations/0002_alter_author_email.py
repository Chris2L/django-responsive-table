# Generated by Django 4.2.3 on 2023-07-28 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="email",
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]