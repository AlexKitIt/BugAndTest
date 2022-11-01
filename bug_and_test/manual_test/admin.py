from django.contrib import admin
from .models import TestSuite, Test, Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


admin.site.register(Test)
admin.site.register(TestSuite)
