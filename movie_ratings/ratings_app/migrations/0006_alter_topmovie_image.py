# Generated by Django 3.2 on 2021-04-26 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings_app', '0005_alter_topmovie_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topmovie',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]