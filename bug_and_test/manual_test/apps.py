from django.apps import AppConfig


class ManualTestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'manual_test'
    verbose_name = 'Приложение по контролю тестирования'
