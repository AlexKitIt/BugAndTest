
from django.contrib.auth.models import User
from django.db import models

from django.urls import reverse
from slugify import slugify


class TestSuite(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название test-suite')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def save(self,  *args, **kwargs):
        self.slug = slugify(self.name)
        return super(TestSuite, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('ts_cat', kwargs={'ts_slug': self.slug})

    class Meta:
        verbose_name = 'Test-suite'
        verbose_name_plural = 'Test-suites'


class Test(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название теста')
    preconditions = models.TextField(blank=True, verbose_name='Предусловия')
    steps = models.TextField(blank=True, verbose_name='Шаги теста')
    result = models.TextField(blank=True, verbose_name='Ожидаемый результат')
    code = models.FileField(upload_to='manual_test/code/', verbose_name='Код автотеста', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET('Пользователь удален'), verbose_name='Test-suite')
    test_suite = models.ForeignKey(TestSuite, on_delete=models.CASCADE, verbose_name='Test-suite')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    email = models.EmailField(max_length=200, verbose_name='Email')
    message = models.TextField(blank=True, verbose_name='Сообщение')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
