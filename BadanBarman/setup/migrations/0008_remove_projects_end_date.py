# Generated by Django 4.0.2 on 2024-07-16 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0007_projects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='end_date',
        ),
    ]
