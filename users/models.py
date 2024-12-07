import os

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from sorl.thumbnail import ImageField

from games.models import Game


def get_image_path(instance, filename):
    return os.path.join('users', str(instance.id), 'avatar_' + filename)


class User(AbstractUser):
    photo = ImageField(
        upload_to=get_image_path,
        max_length=255,
        blank=True,
        null=True,
    )
    lists = models.ManyToManyField('games.Game', through='UserList')

    def __str__(self):
        return self.username


class ListType(models.Model):
    type = models.CharField('Тип списка', max_length=20)
    translation = models.CharField('Перевод', max_length=20)
    order = models.PositiveSmallIntegerField('Порядок')

    class Meta:
        verbose_name = 'Тип списка'
        verbose_name_plural = 'Типы списков'

    def __str__(self):
        return self.translation


class UserList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(
        'games.Game',
        on_delete=models.CASCADE,
        verbose_name='Игра'
    )
    type = models.ForeignKey(
        ListType,
        on_delete=models.CASCADE,
        verbose_name='Тип списка',
    )
    rate = models.SmallIntegerField(
        blank=True, null=True,
        verbose_name='Оценка',
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text='Оценка от 1 до 10'
    )

    class Meta:
        verbose_name = 'Список'
        verbose_name_plural = 'Списки'
