# Generated by Django 5.0.4 on 2024-05-05 07:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0010_article_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="image",
            field=models.TextField(blank=True, null=True),
        ),
    ]
