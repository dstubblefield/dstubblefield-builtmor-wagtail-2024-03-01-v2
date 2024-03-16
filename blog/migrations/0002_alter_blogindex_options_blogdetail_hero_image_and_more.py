# Generated by Django 5.0.2 on 2024-03-13 17:34

import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail.models
import wagtail.search.index
import wagtail.snippets.blocks
import wagtailmarkdown.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
        ("images", "0002_alter_customimage_caption"),
        (
            "taggit",
            "0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx",
        ),
        ("wagtailcore", "0092_query_searchpromotion_querydailyhits"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blogindex",
            options={
                "verbose_name": "Blog Landing Page",
                "verbose_name_plural": "Blog Landing Pages",
            },
        ),
        migrations.AddField(
            model_name="blogdetail",
            name="hero_image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.customimage",
            ),
        ),
        migrations.AddField(
            model_name="blogdetail",
            name="markdown_field",
            field=wagtailmarkdown.fields.MarkdownField(
                blank=True, null=True, verbose_name="Markdown Field"
            ),
        ),
        migrations.AddField(
            model_name="blogindex",
            name="hero_image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.customimage",
            ),
        ),
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
                        wagtail.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                ("caption", wagtail.blocks.CharBlock(required=False)),
                                (
                                    "quotation",
                                    wagtail.blocks.StructBlock(
                                        [
                                            ("quote", wagtail.blocks.TextBlock()),
                                            (
                                                "attribution",
                                                wagtail.blocks.CharBlock(
                                                    required=False
                                                ),
                                            ),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                ],
                blank=True,
                null=True,
                verbose_name="Body Content",
            ),
        ),
        migrations.AlterField(
            model_name="blogindex",
            name="body",
            field=wagtail.fields.RichTextField(
                blank=True, help_text="This text will appear on the blog landing page"
            ),
        ),
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
                (
                    "live",
                    models.BooleanField(
                        default=True, editable=False, verbose_name="live"
                    ),
                ),
                (
                    "has_unpublished_changes",
                    models.BooleanField(
                        default=False,
                        editable=False,
                        verbose_name="has unpublished changes",
                    ),
                ),
                (
                    "first_published_at",
                    models.DateTimeField(
                        blank=True,
                        db_index=True,
                        null=True,
                        verbose_name="first published at",
                    ),
                ),
                (
                    "last_published_at",
                    models.DateTimeField(
                        editable=False, null=True, verbose_name="last published at"
                    ),
                ),
                (
                    "go_live_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="go live date/time"
                    ),
                ),
                (
                    "expire_at",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="expiry date/time"
                    ),
                ),
                (
                    "expired",
                    models.BooleanField(
                        default=False, editable=False, verbose_name="expired"
                    ),
                ),
                (
                    "locked",
                    models.BooleanField(
                        default=False, editable=False, verbose_name="locked"
                    ),
                ),
                (
                    "locked_at",
                    models.DateTimeField(
                        editable=False, null=True, verbose_name="locked at"
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("bio", models.TextField()),
                (
                    "latest_revision",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailcore.revision",
                        verbose_name="latest revision",
                    ),
                ),
                (
                    "live_revision",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailcore.revision",
                        verbose_name="live revision",
                    ),
                ),
                (
                    "locked_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="locked_%(class)ss",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="locked by",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(
                wagtail.models.PreviewableMixin,
                wagtail.search.index.Indexed,
                models.Model,
            ),
        ),
        migrations.CreateModel(
            name="BlogPageTags",
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
                (
                    "content_object",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tagged_items",
                        to="blog.blogdetail",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(app_label)s_%(class)s_items",
                        to="taggit.tag",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="blogdetail",
            name="tags",
            field=modelcluster.contrib.taggit.ClusterTaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="blog.BlogPageTags",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
