# Generated by Django 2.2.13 on 2020-09-12 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date_posted',
            new_name='published_date',
        ),
    ]
