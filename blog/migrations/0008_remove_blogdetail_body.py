# Generated by Django 5.0.2 on 2024-03-02 02:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0007_blogpagetags_blogdetail_tags"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blogdetail",
            name="body",
        ),
    ]
