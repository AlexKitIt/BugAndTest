# Generated by Django 3.2.7 on 2022-11-01 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
                ('message', models.TextField(blank=True, verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='TestSuite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название test-suite')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Test-suite',
                'verbose_name_plural': 'Test-suites',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название теста')),
                ('preconditions', models.TextField(blank=True, verbose_name='Предусловия')),
                ('steps', models.TextField(blank=True, verbose_name='Шаги теста')),
                ('result', models.TextField(blank=True, verbose_name='Ожидаемый результат')),
                ('code', models.FileField(blank=True, upload_to='manual_test/code/', verbose_name='Код автотеста')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('test_suite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manual_test.testsuite', verbose_name='Test-suite')),
                ('user', models.ForeignKey(on_delete=models.SET('Пользователь удален'), to=settings.AUTH_USER_MODEL, verbose_name='Test-suite')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
            },
        ),
    ]
