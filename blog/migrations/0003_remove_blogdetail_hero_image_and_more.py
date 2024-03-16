# Generated by Django 5.0.2 on 2024-03-15 21:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_blogindex_options_blogdetail_hero_image_and_more"),
        ("images", "0002_alter_customimage_caption"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blogdetail",
            name="hero_image",
        ),
        migrations.RemoveField(
            model_name="blogindex",
            name="hero_image",
        ),
        migrations.AddField(
            model_name="author",
            name="is_contributor",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="blogdetail",
            name="hero_image_desktop",
            field=models.ForeignKey(
                blank=True,
                help_text="Image needs to be landscape 2660-w x1400-h pixels.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.customimage",
            ),
        ),
        migrations.AddField(
            model_name="blogdetail",
            name="hero_image_mobile",
            field=models.ForeignKey(
                blank=True,
                help_text="Image needs to be portrait 800-w x1200-h pixels.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.customimage",
            ),
        ),
        migrations.AddField(
            model_name="blogindex",
            name="hero_image_desktop",
            field=models.ForeignKey(
                blank=True,
                help_text="Image needs to be landscape 2560-w x 1400-h pixels.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.customimage",
            ),
        ),
        migrations.AddField(
            model_name="blogindex",
            name="hero_image_mobile",
            field=models.ForeignKey(
                blank=True,
                help_text="Image needs to be portrait 800-w x12000-h pixels.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.customimage",
            ),
        ),
    ]