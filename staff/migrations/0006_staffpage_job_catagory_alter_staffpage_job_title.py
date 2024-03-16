# Generated by Django 5.0.2 on 2024-03-11 12:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("staff", "0005_alter_staffpage_job_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="staffpage",
            name="job_catagory",
            field=models.CharField(
                blank=True,
                choices=[
                    ("owner", "Owner / CEO"),
                    ("office", "Office Staff"),
                    ("sales", "Sales"),
                    ("project_manager", "Project Manager"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="staffpage",
            name="job_title",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
