# Generated by Django 2.2.4 on 2019-10-10 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifs', '0005_auto_20190914_0513'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='is_base_gif',
            field=models.BooleanField(default=False),
        ),
    ]
