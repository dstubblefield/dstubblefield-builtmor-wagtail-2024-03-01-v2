# Generated by Django 5.0.2 on 2024-03-11 12:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("staff", "0006_staffpage_job_catagory_alter_staffpage_job_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="staffpage",
            name="job_catagory",
            field=models.CharField(
                choices=[
                    ("owner", "Owner / CEO"),
                    ("office", "Office Staff"),
                    ("sales", "Sales"),
                    ("project_manager", "Project Manager"),
                ],
                max_length=255,
            ),
        ),
    ]