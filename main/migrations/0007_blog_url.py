# Generated by Django 4.1.2 on 2022-10-19 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_portfolio_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog", name="url", field=models.URLField(blank=True, null=True),
        ),
    ]
