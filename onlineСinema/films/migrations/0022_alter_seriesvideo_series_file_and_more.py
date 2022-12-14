# Generated by Django 4.1.2 on 2022-11-01 15:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0021_alter_seriesvideo_series_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seriesvideo',
            name='series_file',
            field=models.FileField(upload_to='video/series/<django.db.models.query_utils.DeferredAttribute object at 0x7fe7a2de2590>', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])]),
        ),
        migrations.AlterField(
            model_name='seriesvideo',
            name='series_ind',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.series'),
        ),
    ]
