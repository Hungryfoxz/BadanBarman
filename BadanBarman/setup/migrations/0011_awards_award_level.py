# Generated by Django 4.0.2 on 2024-07-18 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0010_awards_alter_projects_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='awards',
            name='award_level',
            field=models.CharField(choices=[('Local', 'Local'), ('State', 'State'), ('National', 'National'), ('International', 'International')], default='Local', max_length=15),
        ),
    ]
