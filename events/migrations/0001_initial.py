# Generated by Django 2.2 on 2020-02-21 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(help_text='Day of event', verbose_name='Day of event')),
                ('start_time', models.TimeField(help_text='Start time', verbose_name='Staring time')),
                ('end_time', models.TimeField(help_text='End time', verbose_name='End time')),
                ('notes', models.TextField(blank=True, help_text='Text note', null=True, verbose_name='Textual notes')),
            ],
            options={
                'verbose_name': 'Scheduling',
                'verbose_name_plural': 'Scheduling',
            },
        ),
    ]