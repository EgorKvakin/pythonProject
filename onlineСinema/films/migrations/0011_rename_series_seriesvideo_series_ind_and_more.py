# Generated by Django 4.1.2 on 2022-10-31 18:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0010_alter_seriesvideo_series_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seriesvideo',
            old_name='series',
            new_name='series_ind',
        ),
        migrations.AlterField(
            model_name='seriesvideo',
            name='series_file',
            field=models.FileField(upload_to='video/series/<django.db.models.query_utils.DeferredAttribute object at 0x7f0f446b3ac0>', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])]),
        ),
    ]
