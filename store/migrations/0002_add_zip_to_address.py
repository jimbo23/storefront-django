# Generated by Django 4.1.1 on 2022-09-26 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="zip",
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]