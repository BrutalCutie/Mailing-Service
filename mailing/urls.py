from mailing import views

from mailing.apps import MailingConfig

from django.urls import path

app_name = MailingConfig.name


urlpatterns = [
    path('', views.main_page, name='main_page')
]
