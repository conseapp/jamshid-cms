# Generated by Django 5.0.1 on 2024-01-18 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post__extracted_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='_extracted_body',
            new_name='extracted_body',
        ),
    ]