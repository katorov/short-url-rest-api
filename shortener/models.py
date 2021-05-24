from django.db import models
from django.conf import settings


class TimestampModel(models.Model):
    """Абстрактная модель с полями даты создания и даты изменения"""
    created_at = models.DateTimeField('Дата создания', auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField('Дата изменения', auto_now=True, db_index=True)

    class Meta:
        abstract = True
        ordering = ['created_at']


class ShortLink(TimestampModel):
    """Короткая ссылка"""
    url = models.URLField('Полная ссылка')

    class Meta:
        verbose_name = 'Короткая ссылка'
        verbose_name_plural = 'Короткие ссылки'

    @property
    def short_url(self):
        return f'{settings.BASE_SHORT_HOST}/{self.id}'

    def __str__(self):
        return f'{self.short_url}'
