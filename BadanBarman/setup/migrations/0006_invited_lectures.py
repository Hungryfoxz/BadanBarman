# Generated by Django 4.0.2 on 2024-07-16 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0005_alter_research_scholars_enrollment_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invited_Lectures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Please provide only the title...', max_length=150)),
                ('date', models.CharField(help_text='Please use the following format: <em>first three letters of month [.] DD,YYYY</em>. Eg: Sep.21,2021', max_length=12)),
                ('event', models.CharField(help_text='Name of the Event on which the lecture was delivered...', max_length=200)),
                ('organizer', models.CharField(help_text='Name of the programme where the Lecture was held...', max_length=100)),
                ('location', models.CharField(help_text='Please follow the below format [ Provide any 2 ]: Locality,District,State,Country...', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Invited Lectures',
            },
        ),
    ]
