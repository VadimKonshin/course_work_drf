from django.db import models

from config import settings
from user.models import NULLABLE


class Habit(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Создатель привычки')
    place = models.CharField(max_length=255, verbose_name='Место', **NULLABLE)
    time = models.DateTimeField(verbose_name='Время')
    action = models.CharField(max_length=255, verbose_name='Действие')
    is_pleasant = models.BooleanField(default=True, verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Связанная привычка', **NULLABLE)
    reward = models.CharField(max_length=255, verbose_name='Вознагрождение', **NULLABLE)
    periodicity = models.PositiveIntegerField(default=1, verbose_name='Переодичность')
    time_to_complete = models.PositiveIntegerField(verbose_name='Время на выполнение')
    is_public = models.BooleanField(default=True, verbose_name='Публичность')

    def __str__(self):
        return f'{self.owner}, {self.related_habit}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'