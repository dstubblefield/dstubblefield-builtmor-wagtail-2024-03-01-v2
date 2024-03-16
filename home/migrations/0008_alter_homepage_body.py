# Generated by Django 5.0.2 on 2024-03-16 04:22

import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0007_alter_homepage_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "rich_text",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "RichText",
                                    wagtail.blocks.RichTextBlock(
                                        features=[
                                            "h2",
                                            "h3",
                                            "bold",
                                            "italic",
                                            "ol",
                                            "ul",
                                            "link",
                                            "blockquote",
                                        ]
                                    ),
                                )
                            ]
                        ),
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
                                                    help_text="Image needs to be landscape 2560-w x 1400-h pixels."
                                                ),
                                            ),
                                            (
                                                "image_mobile",
                                                wagtail.images.blocks.ImageChooserBlock(
                                                    help_text="Image needs to be portraits 800-w x 1,200-h pixels."
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
                    (
                        "hero",
                        wagtail.blocks.StreamBlock(
                            [
                                (
                                    "hero",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "image_desktop",
                                                wagtail.images.blocks.ImageChooserBlock(
                                                    help_text="Image needs to be landscape 2560-w x 1400-h pixels."
                                                ),
                                            ),
                                            (
                                                "image_mobile",
                                                wagtail.images.blocks.ImageChooserBlock(
                                                    help_text="Image needs to be portraits 800w x 1,200h pixels."
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
                    (
                        "video",
                        wagtail.blocks.StructBlock(
                            [("video", wagtail.embeds.blocks.EmbedBlock())]
                        ),
                    ),
                    (
                        "cta",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "text",
                                    wagtail.blocks.RichTextBlock(
                                        features=["bold", "italic"]
                                    ),
                                ),
                                (
                                    "button",
                                    wagtail.blocks.CharBlock(
                                        help_text="Button text",
                                        max_length=100,
                                        required=True,
                                    ),
                                ),
                                (
                                    "page_chooser",
                                    wagtail.blocks.PageChooserBlock(required=True),
                                ),
                            ]
                        ),
                    ),
                ],
                blank=True,
                null=True,
            ),
        ),
    ]
