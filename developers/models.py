from django.db import models


class Developer(models.Model):
    name = models.CharField('Название', max_length=255)
    country = models.CharField('Страна', max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Разработчик'
        verbose_name_plural = 'Разработчики'

    def __str__(self):
        return self.name
