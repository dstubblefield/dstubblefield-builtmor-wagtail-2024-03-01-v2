# Generated by Django 5.0.2 on 2024-03-10 18:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("staff", "0002_remove_staffindex_category_hero_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="staffindex",
            name="subtitle",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
