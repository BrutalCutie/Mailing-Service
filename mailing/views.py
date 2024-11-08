import json
from pprint import pprint

from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import AnonymousUser

from mailing import forms
from mailing.models import Mailing, Receiver, Message
from users.models import MailingUser
from mailing.services import MailingService


class MailingListView(ListView):
    model = Mailing
    template_name = 'mailing/main_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        if user.is_authenticated:
            context['created'] = user.mailings.filter(status="Создана")
            context['started'] = user.mailings.filter(status="Запущена")
            context['finished'] = user.mailings.filter(status="Завершена")

        return context


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
        context['back_page'] = self.request.environ['HTTP_REFERER']

        return context


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = forms.MailingForm
    template_name = 'mailing/mailing_new.html'

    def get_success_url(self):
        return reverse("mailing:mailing_detail", kwargs={"pk": self.object.pk})


class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = 'mailing/mailing_delete_confirm.html'
    success_url = reverse_lazy("mailing:main_page")


class ReceiverListView(ListView):
    model = Receiver
    template_name = 'mailing/receiver_list.html'

    context_object_name = 'receivers'

    def get_queryset(self):
        user = self.request.user
        queryset = user.receivers.all()

        return queryset


class ReceiverCreateView(CreateView):
    model = Receiver
    form_class = forms.ReceiverForm
    template_name = 'mailing/receiver_new.html'
    success_url = reverse_lazy("mailing:receiver_list")

    def form_valid(self, form):
        receiver = form.save()
        user = self.request.user
        receiver.owner = user
        user.save()

        return super().form_valid(form)


class ReceiverDetailView(DetailView):
    model = Receiver
    template_name = 'mailing/receiver_detail.html'
    context_object_name = 'receiver'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['back_page'] = self.request.environ['HTTP_REFERER']

        return context


class ReceiverUpdateView(UpdateView):
    model = Receiver
    form_class = forms.ReceiverForm
    template_name = 'mailing/receiver_new.html'

    def get_success_url(self):
        return reverse("mailing:receiver_detail", kwargs={"pk": self.object.pk})


class ReceiverDeleteView(DeleteView):
    model = Receiver
    template_name = 'mailing/receiver_confirm_delete.html'
    success_url = reverse_lazy("mailing:receiver_list")


class MessageListView(ListView):
    model = Message
    template_name = 'mailing/message_list.html'

    context_object_name = 'messages'

    def get_queryset(self):
        user = self.request.user
        queryset = user.messages.all()

        return queryset


class MessageCreateView(CreateView):
    model = Message
    form_class = forms.MessageForm
    template_name = 'mailing/message_new.html'
    success_url = reverse_lazy("mailing:message_new")

    def form_valid(self, form):
        receiver = form.save()
        user = self.request.user
        receiver.owner = user
        user.save()

        return super().form_valid(form)


class MessageDetailView(DetailView):
    model = Message
    template_name = 'mailing/message_detail.html'
    context_object_name = 'message'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['back_page'] = self.request.environ['HTTP_REFERER']

        return context


class MessageUpdateView(UpdateView):
    model = Message
    form_class = forms.MessageForm
    template_name = 'mailing/message_new.html'

    def get_success_url(self):
        return reverse("mailing:message_detail", kwargs={"pk": self.object.pk})


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'mailing/message_confirm_delete.html'
    success_url = reverse_lazy("mailing:message_list")