# Generated by Django 4.1.2 on 2022-11-01 18:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0023_alter_seriesvideo_series_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='seriesvideo',
            name='series_index',
            field=models.IntegerField(default=0, verbose_name='Номер серии'),
        ),
        migrations.AlterField(
            model_name='seriesvideo',
            name='series_file',
            field=models.FileField(upload_to='video/series/<django.db.models.query_utils.DeferredAttribute object at 0x7f594bb8a500>', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])]),
        ),
    ]
