# Generated by Django 4.1.2 on 2022-11-01 15:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0018_remove_seriesvideo_series_ind_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='seriesvideo',
            name='series_ind',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='films.series'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='seriesvideo',
            name='series_file',
            field=models.FileField(upload_to='video/series/<django.db.models.query_utils.DeferredAttribute object at 0x7f0df951fac0>', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])]),
        ),
    ]
