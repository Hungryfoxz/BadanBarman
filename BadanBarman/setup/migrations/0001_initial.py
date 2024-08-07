# Generated by Django 4.0.2 on 2024-07-02 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Websites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=120)),
                ('category', models.CharField(max_length=100)),
                ('dateOfDevelopment', models.DateTimeField()),
                ('framework', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Websites',
            },
        ),
    ]
