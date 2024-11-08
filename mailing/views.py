from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from mailing import forms
from mailing.models import Mailing
from users.models import MailingUser
from mailing.services import MailingService


class MainPageView(ListView):
    model = Mailing
    template_name = 'mailing/main_page.html'

    context_object_name = 'mailings'

    def get_queryset(self):
        user = self.request.user
        queryset = user.mailings.all()

        print(queryset)

        return queryset


class MailingCreateView(CreateView):
    model = Mailing
    form_class = forms.MailingForm
    template_name = 'mailing/mailing_new.html'
    success_url = reverse_lazy("mailing:main_page")

    def form_valid(self, form):
        mailing = form.save()
        user = self.request.user
        mailing.owner = user
        user.save()

        return super().form_valid(form)


class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'mailing/mailing_detail.html'
    context_object_name = 'mailing'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mailing_pk = self.kwargs['pk']

        context['receivers_list'] = MailingService.get_sreceivers(mailing_pk)

        return context
