from django.db import models


# TODO: Add comments and lists.

class Developer(models.Model):
    name = models.CharField('Название', max_length=255)
    country = models.CharField('Страна', max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Разработчик'
        verbose_name_plural = 'Разработчики'

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField('Название', max_length=255)
    country = models.CharField('Страна', max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', blank=True, null=True)
    release_date = models.DateField('Дата выхода')
    rating = models.FloatField('Рейтинг', default=0)
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
    genres = models.ManyToManyField(Genre, verbose_name='Жанры')

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

    def __str__(self):
        return self.name
