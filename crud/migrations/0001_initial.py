# Generated by Django 2.2 on 2020-02-25 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='메세지의 제목', max_length=120)),
                ('message', models.TextField(help_text='니 생각은 어때?')),
            ],
        ),
    ]
