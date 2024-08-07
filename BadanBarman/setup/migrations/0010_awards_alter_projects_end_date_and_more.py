# Generated by Django 4.0.2 on 2024-07-18 06:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0009_projects_end_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_the_awardees', models.CharField(max_length=80)),
                ('name_of_the_award', models.CharField(max_length=100)),
                ('conferred_on', models.CharField(help_text='Please use the following format: <em>DD[space]MONTH-NAME,[space]YYYY</em>.Eg:21 March, 2019', max_length=20)),
                ('awarding_agency', models.CharField(max_length=80)),
                ('image', models.ImageField(blank=True, default='static/gallary/awards/default.jpg', upload_to='static/gallary/awards/')),
            ],
            options={
                'verbose_name_plural': 'Awards',
            },
        ),
        migrations.AlterField(
            model_name='projects',
            name='end_date',
            field=models.CharField(default=django.utils.timezone.now, help_text='Format : DD[th]_Month,_YYYY  ; Example : 19th March, 2019', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projects',
            name='other_persons',
            field=models.CharField(default='NA', help_text='Use a comma separated list : name1, name2, name3...', max_length=100),
        ),
    ]
