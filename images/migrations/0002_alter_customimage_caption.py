# Generated by Django 5.0.2 on 2024-03-10 14:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("images", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customimage",
            name="caption",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]