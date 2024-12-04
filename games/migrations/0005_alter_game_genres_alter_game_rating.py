# Generated by Django 5.1.3 on 2024-12-03 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_game_poster_game_video_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='genres',
            field=models.ManyToManyField(blank=True, to='games.genre', verbose_name='Жанры'),
        ),
        migrations.AlterField(
            model_name='game',
            name='rating',
            field=models.FloatField(blank=True, default=0, verbose_name='Рейтинг'),
        ),
    ]
