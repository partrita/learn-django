# Generated by Django 2.2 on 2020-02-25 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.FloatField()),
                ('measurement_unit', models.CharField(choices=[('0', 'Meters'), ('1', 'Milimeters'), ('2', 'Centimeters'), ('3', 'Liters'), ('4', 'Mililiters'), ('5', 'Unit')], max_length=2)),
            ],
        ),
    ]