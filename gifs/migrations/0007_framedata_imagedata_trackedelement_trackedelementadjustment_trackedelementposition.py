# Generated by Django 2.2.4 on 2019-11-17 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gifs', '0006_image_is_base_gif'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=1000)),
                ('background_image_path', models.CharField(max_length=10000)),
                ('foreground_image_path', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='TrackedElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('image_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gifs.ImageData')),
            ],
        ),
        migrations.CreateModel(
            name='TrackedElementPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField(blank=True, null=True)),
                ('y', models.IntegerField(blank=True, null=True)),
                ('z', models.IntegerField(blank=True, null=True)),
                ('width', models.IntegerField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('rotation', models.IntegerField(blank=True, null=True)),
                ('brightness', models.IntegerField(blank=True, null=True)),
                ('tracked_element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gifs.TrackedElement')),
            ],
        ),
        migrations.CreateModel(
            name='FrameData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('image_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gifs.ImageData')),
            ],
        ),
        migrations.CreateModel(
            name='TrackedElementAdjustment',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('gifs.trackedelementposition',),
        ),
    ]
