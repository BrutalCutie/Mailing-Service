from django.shortcuts import render
from django.views.generic import TemplateView, View


class MainPageView(TemplateView):
    template_name = 'mailing/main_page.html'

