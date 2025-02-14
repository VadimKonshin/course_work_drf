# Generated by Django 5.1 on 2024-08-30 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(blank=True, max_length=255, null=True, verbose_name='Место')),
                ('time', models.DateTimeField(verbose_name='Время')),
                ('action', models.CharField(max_length=255, verbose_name='Действие')),
                ('is_pleasant', models.BooleanField(default=True, verbose_name='Признак приятной привычки')),
                ('reward', models.CharField(blank=True, max_length=255, null=True, verbose_name='Вознагрождение')),
                ('periodicity', models.PositiveIntegerField(default=1, verbose_name='Переодичность')),
                ('time_to_complete', models.PositiveIntegerField(verbose_name='Время на выполнение')),
                ('is_public', models.BooleanField(default=True, verbose_name='Публичность')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
    ]
