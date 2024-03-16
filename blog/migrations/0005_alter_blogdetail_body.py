# Generated by Django 5.0.2 on 2024-03-15 23:40

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail.snippets.blocks
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_blogdetail_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogdetail",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "author",
                        wagtail.snippets.blocks.SnippetChooserBlock("blog.Author"),
                    ),
                    (
                        "carousel",
                        wagtail.blocks.StreamBlock(
                            [
                                (
                                    "slide",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "image_desktop",
                                                wagtail.images.blocks.ImageChooserBlock(
                                                    help_text="Image needs to be landscape 2560-w x1400-h pixels."
                                                ),
                                            ),
                                            (
                                                "image_mobile",
                                                wagtail.images.blocks.ImageChooserBlock(
                                                    help_text="Image needs to be portraits 800w x 1,200-h pixels."
                                                ),
                                            ),
                                            ("title", wagtail.blocks.CharBlock()),
                                            ("text", wagtail.blocks.TextBlock()),
                                            ("button", wagtail.blocks.CharBlock()),
                                            (
                                                "page_chooser",
                                                wagtail.blocks.PageChooserBlock(
                                                    required=False
                                                ),
                                            ),
                                        ]
                                    ),
                                )
                            ]
                        ),
                    ),
                ],
                blank=True,
                null=True,
                verbose_name="Body Content",
            ),
        ),
    ]