# Generated by Django 5.0.2 on 2024-03-15 19:45

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("images", "0002_alter_customimage_caption"),
        ("products", "0004_remove_productpage_product_hero_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="productscategorypage",
            name="subcategory_hero",
        ),
        migrations.RemoveField(
            model_name="productsindex",
            name="category_hero",
        ),
        migrations.AddField(
            model_name="productscategorypage",
            name="subcategory_hero_desktop",
            field=models.ForeignKey(
                blank=True,
                help_text="Image needs to be landscape 1920-w x1080-h pixels.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.customimage",
            ),
        ),
        migrations.AddField(
            model_name="productscategorypage",
            name="subcategory_hero_mobile",
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
            model_name="productsindex",
            name="category_hero_desktop",
            field=models.ForeignKey(
                blank=True,
                help_text="Image needs to be landscape 1920-w x1080-h pixels.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.customimage",
            ),
        ),
        migrations.AddField(
            model_name="productsindex",
            name="category_hero_mobile",
            field=models.ForeignKey(
                blank=True,
                help_text="Image needs to be portrait 800-w x1200-h pixels.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.customimage",
            ),
        ),
        migrations.AlterField(
            model_name="productpage",
            name="description",
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name="productpage",
            name="product_hero_desktop",
            field=models.ForeignKey(
                blank=True,
                help_text="Image needs to be landscape 1920-w x1080-h pixels.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.customimage",
            ),
        ),
        migrations.AlterField(
            model_name="productpage",
            name="product_hero_mobile",
            field=models.ForeignKey(
                blank=True,
                help_text="Image needs to be portraits 800-w x 1,200-h pixels.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.customimage",
            ),
        ),
        migrations.AlterField(
            model_name="productscategorypage",
            name="details",
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name="productsindex",
            name="description",
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]
