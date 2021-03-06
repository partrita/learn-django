# Generated by Django 2.2.13 on 2020-09-13 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=20)),
                ('model_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('contact', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('start_date', models.DateTimeField(help_text='Start time', verbose_name='Staring time')),
                ('end_date', models.DateTimeField(help_text='End time', verbose_name='End time')),
                ('notes', models.TextField(blank=True, help_text='Text note', null=True, verbose_name='Textual notes')),
                ('equip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Equipment')),
            ],
        ),
        migrations.AddField(
            model_name='equipment',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Manager'),
        ),
    ]
