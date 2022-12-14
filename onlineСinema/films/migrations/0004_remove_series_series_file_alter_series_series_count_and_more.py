# Generated by Django 4.1.2 on 2022-10-25 10:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_series'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='series',
            name='series_file',
        ),
        migrations.AlterField(
            model_name='series',
            name='series_count',
            field=models.PositiveBigIntegerField(verbose_name='Кол-во серий'),
        ),
        migrations.CreateModel(
            name='SeriesVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series_file', models.FileField(upload_to='video/series/<django.db.models.query_utils.DeferredAttribute object at 0x0000024244C76F40>', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])])),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.series')),
            ],
        ),
    ]
