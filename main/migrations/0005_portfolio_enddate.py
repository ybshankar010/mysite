# Generated by Django 4.1.2 on 2022-10-19 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_remove_skill_is_key_skill_skill_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="portfolio",
            name="enddate",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
