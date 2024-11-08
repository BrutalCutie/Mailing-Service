import json
from pprint import pprint

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from mailing import forms
from mailing.models import Mailing, Receiver, Message
from users.models import MailingUser
from mailing.services import MailingService


class MailingListView(ListView):
    model = Mailing
    template_name = 'mailing/main_page.html'

    context_object_name = 'mailings'

    def get_queryset(self):
        user = self.request.user
        queryset = user.mailings.all()

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


class MailingUpdateView(UpdateView):
    pass


class MailingDeleteView(DeleteView):
    pass


class ReceiverListView(ListView):
    model = Receiver
    template_name = 'mailing/receiver_list.html'

    context_object_name = 'receivers'

    def get_queryset(self):
        user = self.request.user
        queryset = user.receivers.all()

        return queryset


class ReceiverCreateView(CreateView):
    pass


class ReceiverDetailView(DetailView):
    model = Receiver
    template_name = 'mailing/receiver_detail.html'
    context_object_name = 'receiver'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['back_page'] = self.request.environ['HTTP_REFERER']

        return context


class ReceiverUpdateView(UpdateView):
    pass


class ReceiverDeleteView(DeleteView):
    pass




