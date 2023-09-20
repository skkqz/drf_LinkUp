from django.db import models


class Organization(models.Model):
    """
    Модель организаций.
    """

    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(max_length=500, verbose_name='Описание')

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return self.name
