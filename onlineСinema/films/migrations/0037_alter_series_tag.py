# Generated by Django 4.1.2 on 2022-11-05 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0036_alter_film_tag_alter_series_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='tag',
            field=models.CharField(choices=[('a', 'Hola'), ('b', 'Hello'), ('c', 'Bonjour'), ('d', 'Boas')], default='Сериал', max_length=1, verbose_name='Тэг'),
        ),
    ]
