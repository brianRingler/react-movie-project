# Generated by Django 3.2 on 2021-04-25 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings_app', '0003_auto_20210425_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topmovie',
            name='release_date',
            field=models.CharField(max_length=4),
        ),
    ]
