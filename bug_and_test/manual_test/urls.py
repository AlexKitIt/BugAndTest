from django.conf import settings
from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

from .views import ContactCreate


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='manual_test/logout.html'), name='logout'),

    path('mail_admin/', ContactCreate.as_view(template_name='manual_test/mail_admin.html'), name='mail_admin'),
    path('success/', views.success, name='success_page'),

    path('test_create/', views.create_test, name='create_test'),
    path('ts_create/', views.create_test_suite, name='create_ts'),

    path('tests/', views.test, name='tests'),
    path('tests/<slug:ts_slug>/', views.test, name='ts_cat'),
    path('test/<int:test_id>/', views.get_one_test, name='one_test'),
    path('test/<int:test_id>/edit', views.edit_test, name='edit_test'),
    path('test/<int:test_id>/delete', views.delete_test, name='delete_test'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
