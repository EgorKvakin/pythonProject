# Generated by Django 4.1.1 on 2022-09-26 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0006_alter_film_film_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='film_preview',
            field=models.ImageField(upload_to='images/images/films/', verbose_name='Превью фильма'),
        ),
    ]
