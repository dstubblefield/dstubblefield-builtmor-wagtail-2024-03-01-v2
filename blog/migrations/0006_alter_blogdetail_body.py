# Generated by Django 5.0.2 on 2024-03-01 21:26

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0005_alter_blogindex_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogdetail",
            name="body",
            field=wagtail.fields.RichTextField(
                blank=True, help_text="This text will appear on the blog landing page"
            ),
        ),
    ]