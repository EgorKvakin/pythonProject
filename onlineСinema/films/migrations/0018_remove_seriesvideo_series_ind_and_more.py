# Generated by Django 4.1.2 on 2022-11-01 15:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0017_alter_seriesvideo_series_file_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seriesvideo',
            name='series_ind',
        ),
        migrations.AlterField(
            model_name='seriesvideo',
            name='series_file',
            field=models.FileField(upload_to='video/series/<django.db.models.query_utils.DeferredAttribute object at 0x7f6593453a90>', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])]),
        ),
    ]
