# Generated by Django 5.0.1 on 2024-01-18 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='_extracted_body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
