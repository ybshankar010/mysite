# Generated by Django 4.1.2 on 2022-10-19 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_alter_blog_options_alter_certificate_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
