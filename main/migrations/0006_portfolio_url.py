# Generated by Django 4.1.2 on 2022-10-19 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_portfolio_enddate"),
    ]

    operations = [
        migrations.AddField(
            model_name="portfolio",
            name="url",
            field=models.URLField(blank=True, null=True),
        ),
    ]
