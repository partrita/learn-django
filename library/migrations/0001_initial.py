# Generated by Django 2.2 on 2020-03-05 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='')),
                ('author', models.CharField(default='anonymous', max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('describe', models.TextField()),
            ],
        ),
    ]