from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from mailing import forms
from mailing.models import Mailing, Receiver, Message, MailingAttempt
from mailing.services import MailingService


class MailingListView(ListView):
    model = Mailing
    template_name = 'mailing/main_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        if user.is_authenticated:
            context['created'] = MailingService.get_created_mailing(user)
            context['started'] = MailingService.get_started_mailing(user)
            context['finished'] = MailingService.get_finished_mailing(user)

        return context


class MailingCreateView(LoginRequiredMixin, CreateView):
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


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing
    template_name = 'mailing/mailing_detail.html'
    context_object_name = 'mailing'

    def get(self, request, *args, **kwargs):
        query_item = self.model.objects.get(pk=self.kwargs['pk'])

        can_view = [
            request.user == query_item.owner
        ]

        if not any(can_view):
            return redirect('mailing:access_denied')

        return super().get(request, *args, **kwargs)


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = forms.MailingForm
    template_name = 'mailing/mailing_new.html'

    def get_success_url(self):
        return reverse("mailing:mailing_detail", kwargs={"pk": self.object.pk})

    def get(self, request, *args, **kwargs):
        query_item = self.model.objects.get(pk=self.kwargs['pk'])

        can_view = [
            request.user == query_item.owner
        ]

        if not any(can_view):
            return redirect('mailing:access_denied')

        return super().get(request, *args, **kwargs)


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    template_name = 'mailing/mailing_delete_confirm.html'
    success_url = reverse_lazy("mailing:main_page")

    def get(self, request, *args, **kwargs):
        query_item = self.model.objects.get(pk=self.kwargs['pk'])

        can_view = [
            request.user == query_item.owner
        ]

        if not any(can_view):
            return redirect('mailing:access_denied')

        return super().get(request, *args, **kwargs)


class ReceiverListView(LoginRequiredMixin, ListView):
    model = Receiver
    template_name = 'mailing/receiver_list.html'

    context_object_name = 'receivers'

    def get_queryset(self):
        user = self.request.user
        queryset = user.receivers.all()

        return queryset


class ReceiverCreateView(LoginRequiredMixin, CreateView):
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


class ReceiverDetailView(LoginRequiredMixin, DetailView):
    model = Receiver
    template_name = 'mailing/receiver_detail.html'
    context_object_name = 'receiver'

    def get(self, request, *args, **kwargs):
        query_item = self.model.objects.get(pk=self.kwargs['pk'])

        can_view = [
            request.user == query_item.owner
        ]

        if not any(can_view):
            return redirect('mailing:access_denied')

        return super().get(request, *args, **kwargs)


class ReceiverUpdateView(LoginRequiredMixin, UpdateView):
    model = Receiver
    form_class = forms.ReceiverForm
    template_name = 'mailing/receiver_new.html'

    def get_success_url(self):
        return reverse("mailing:receiver_detail", kwargs={"pk": self.object.pk})


class ReceiverDeleteView(LoginRequiredMixin, DeleteView):
    model = Receiver
    template_name = 'mailing/receiver_confirm_delete.html'
    success_url = reverse_lazy("mailing:receiver_list")


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'mailing/message_list.html'

    context_object_name = 'messages'

    def get_queryset(self):
        user = self.request.user
        queryset = user.messages.all()

        return queryset


class MessageCreateView(LoginRequiredMixin, CreateView):
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


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = 'mailing/message_detail.html'
    context_object_name = 'message'

    def get(self, request, *args, **kwargs):
        query_item = self.model.objects.get(pk=self.kwargs['pk'])

        can_view = [
            request.user == query_item.owner
        ]

        if not any(can_view):
            return redirect('mailing:access_denied')

        return super().get(request, *args, **kwargs)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = forms.MessageForm
    template_name = 'mailing/message_new.html'

    def get_success_url(self):
        return reverse("mailing:message_detail", kwargs={"pk": self.object.pk})

    def get(self, request, *args, **kwargs):
        query_item = self.model.objects.get(pk=self.kwargs['pk'])

        can_view = [
            request.user == query_item.owner
        ]

        if not any(can_view):
            return redirect('mailing:access_denied')

        return super().get(request, *args, **kwargs)


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    template_name = 'mailing/message_confirm_delete.html'
    success_url = reverse_lazy("mailing:message_list")

    def get(self, request, *args, **kwargs):
        query_item = self.model.objects.get(pk=self.kwargs['pk'])

        can_view = [
            request.user == query_item.owner
        ]

        if not any(can_view):
            return redirect('mailing:access_denied')

        return super().get(request, *args, **kwargs)


class AcessDenied(TemplateView):
    template_name = 'mailing/access_denied.html'

    def get(self, request, *args, **kwargs):
        print(f"{request.user} Пытался получить доступ к запрещённому контенту")
        return super().get(request, *args, **kwargs)


class AttemptListView(ListView):
    model = MailingAttempt
    template_name = 'mailing/attempt_list.html'
    context_object_name = 'attempts'

    def get_queryset(self):
        user = self.request.user
        user_mailings = user.mailings.filter(status="Создана")

        attempts = []

        for x in user_mailings:
            attempts.extend(x.mailingattempt_set.all())
        return attempts


class AttemptDetailView(DetailView):
    model = MailingAttempt
    template_name = 'mailing/attempt_detail.html'
    context_object_name = 'attempt'
