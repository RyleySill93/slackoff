# Generated by Django 2.2.4 on 2019-11-18 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gifs', '0011_auto_20191118_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackedelementposition',
            name='frame_data',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gifs.FrameData'),
        ),
    ]
