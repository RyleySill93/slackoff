# Generated by Django 2.2.4 on 2019-11-18 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifs', '0008_auto_20191118_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagedata',
            name='background_image_path',
            field=models.CharField(default=1, max_length=10000),
            preserve_default=False,
        ),
    ]
