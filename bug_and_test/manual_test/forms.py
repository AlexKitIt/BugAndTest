from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from django.forms import Textarea
from .models import Contact, Test, TestSuite
from django import forms


class AccountSignInForm(AuthenticationForm):
   username = forms.CharField(widget=forms.TextInput(), label='Логин')
   password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')


class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'message': Textarea(attrs={'placeholder': 'Напишите Ваше сообщение Администратору'})
        }


class TestForm(ModelForm):

    class Meta:
        model = Test
        fields = ['test_suite', 'name', 'preconditions', 'steps', 'result', 'code', ]
        widgets = {
            'name': Textarea(),
            'preconditions': Textarea(),
            'steps': Textarea(),
            'result': Textarea(),
        }


class TestSuiteForm(ModelForm):

    class Meta:
        model = TestSuite
        fields = ['name']
