from django.conf import settings
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Well(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(upload_to='lesson/', verbose_name='превью', **NULLABLE)
    users = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Пользователь')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(upload_to='lesson/', verbose_name='превью', **NULLABLE)
    video_url = models.URLField(verbose_name='ссылка на видео', **NULLABLE)
    well = models.ForeignKey(Well, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE,
                             related_name='lessons')
    users = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Пользователь')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Subscription(models.Model):
    users = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Пользователь'
    )
    well = models.ForeignKey(Well, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE, related_name='well_sub')

    def __str__(self):
        return f'{self.users.name}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
