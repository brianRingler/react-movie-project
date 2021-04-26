# Generated by Django 3.2 on 2021-04-25 22:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings_app', '0002_topmovie'),
    ]

    operations = [
        migrations.AddField(
            model_name='topmovie',
            name='rank',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(251)]),
        ),
        migrations.AlterField(
            model_name='topmovie',
            name='image',
            field=models.ImageField(height_field=67, upload_to='', width_field=45),
        ),
        migrations.AlterField(
            model_name='topmovie',
            name='rating',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='topmovie',
            name='release_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='topmovie',
            name='title',
            field=models.CharField(max_length=125),
        ),
    ]