from django.db import models

from developers.models import Developer
from publishers.models import Publisher
import os

# TODO: Add comments and lists.


class Genre(models.Model):
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


def get_poster_path(instance, filename):
    return os.path.join('games', str(instance.id), 'poster_' + filename)


class Game(models.Model):
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', blank=True, null=True)
    release_date = models.DateField('Дата выхода')
    rating = models.FloatField('Рейтинг', default=0, blank=True)
    developer = models.ForeignKey(
        Developer,
        on_delete=models.CASCADE,
        related_name='games',
        verbose_name='Разработчик'
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE,
        related_name='games',
        null=True,
        blank=True,
        verbose_name='Издатель'
    )
    genres = models.ManyToManyField(Genre, verbose_name='Жанры', blank=True)
    comments = models.ManyToManyField('users.User', through='Comment')
    poster = models.ImageField(
        upload_to=get_poster_path,
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Постер'
    )
    video_url = models.URLField(
        verbose_name='Видео (ссылка)',
        blank=True,
        null=True
    )

    def recalculate_rating(self):
        new_rating = self.userlist_set.aggregate(
            models.Avg('rate', default=0)
        )['rate__avg']

        self.rating = new_rating
        self.save()

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Игра')
    text = models.TextField('Текст')
    created_at = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
