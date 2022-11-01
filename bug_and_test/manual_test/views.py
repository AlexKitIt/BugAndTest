from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .models import Contact, Test
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .forms import ContactForm, TestForm, TestSuiteForm, AccountSignInForm
from manual_test.models import TestSuite


def index(request):
    return render(request, 'manual_test/index.html')


def login_user(request):
    if request.method == "GET":
        return render(request, 'manual_test/login.html', {'form': AccountSignInForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'manual_test/login.html', {'form': AccountSignInForm(),
                                                              'error': 'Указанная связка логин/пароль не найдена'})
        else:
            login(request, user)
            return redirect('index')


def test_suite(request):
    context = {
        'test_suite': TestSuite.objects.all(),
    }
    return render(request, 'manual_test/test_suites.html', context=context)


def test(request, ts_slug=None):
    context = {
        'test_suite': TestSuite.objects.all(),
    }
    tests = ''
    if ts_slug:
        tests = Test.objects.filter(test_suite__slug=ts_slug)
    context.update({'tests': tests})

    return render(request, 'manual_test/tests.html', context=context)


def get_one_test(request, test_id):
    context = {
        'test': Test.objects.get(id=test_id),
    }
    return render(request, 'manual_test/one_test.html', context=context)


@login_required
def edit_test(request, test_id):
    one_test = get_object_or_404(Test, pk=test_id, user=request.user)
    if request.method == "GET":
        context = {
            'form': TestForm(),
            "example": one_test
        }
        return render(request, 'manual_test/edit_test.html', context=context)
    if request.method == "POST":
        old_test = Test.objects.get(id=test_id)
        if request.POST["name"]:
            one_test.name = request.POST["name"]
        else:
            one_test.name = old_test.name
        if request.POST["preconditions"]:
            one_test.preconditions = request.POST["preconditions"]
        else:
            one_test.preconditions = old_test.preconditions
        if request.POST["steps"]:
            one_test.steps = request.POST["steps"]
        else:
            one_test.steps = old_test.steps
        if request.POST["result"]:
            one_test.result = request.POST["result"]
        else:
            one_test.result = old_test.result
        if request.POST["test_suite"]:
            one_test.test_suite = TestSuite.objects.get(pk=request.POST["test_suite"])
        else:
            one_test.test_suite = TestSuite.objects.get(pk=old_test.test_suite)
        one_test.created = timezone.now()
        one_test.user = request.user
        one_test.save()
        context = {
            'test': Test.objects.get(id=test_id),
        }
        return render(request, 'manual_test/one_test.html', context=context)


@login_required
def delete_test(request, test_id):
    one_test = get_object_or_404(Test, pk=test_id, user=request.user)
    if request.method == "POST":
        one_test.delete()
        return redirect('tests')


@login_required
def create_test(request):
    if request.method == "GET":
        return render(request, 'manual_test/create_test.html', {'form': TestForm()})
    else:
        form = TestForm(request.POST, request.FILES)
        new_test = form.save(commit=False)
        new_test.user = request.user
        new_test.save()
        return redirect('tests')


def create_test_suite(request):
    if request.method == "GET":
        context = {
            'test_suite': TestSuite.objects.all(),
            'form': TestSuiteForm()
        }
        return render(request, 'manual_test/create_test_suite.html', context=context)
    else:
        form = TestSuiteForm(request.POST)
        new_test_suite = form.save(commit=False)
        new_test_suite.user = request.user
        new_test_suite.save()
        return redirect('tests')


class ContactCreate(CreateView):
    model = Contact
    success_url = reverse_lazy('success_page')
    form_class = ContactForm

    def form_valid(self, form):
        data = form.data
        subject = f'Message from {data["name"]} Email: {data["email"]}'
        email(subject, data['message'])
        return super().form_valid(form)


def email(subject, content):
    send_mail(subject, content, 'user@gmail.com', ['admin@gmail.com'])


def success(request):
    return render(request, 'manual_test/success_page.html')
