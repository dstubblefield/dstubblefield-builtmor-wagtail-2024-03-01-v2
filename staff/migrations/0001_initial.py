# Generated by Django 5.0.2 on 2024-03-10 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("images", "0002_alter_customimage_caption"),
        ("wagtailcore", "0092_query_searchpromotion_querydailyhits"),
    ]

    operations = [
        migrations.CreateModel(
            name="StaffPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="StaffIndex",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("description", models.TextField(blank=True)),
                (
                    "category_hero",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="images.customimage",
                    ),
                ),
            ],
            options={
                "verbose_name": "Staff",
                "verbose_name_plural": "Staff",
            },
            bases=("wagtailcore.page",),
        ),
    ]
