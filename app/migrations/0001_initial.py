# Generated by Django 3.2.9 on 2021-12-20 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'search_city',
            },
        ),
    ]