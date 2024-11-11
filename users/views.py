from pprint import pprint

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView, TemplateView
from django.core.mail import send_mail
from .forms import MailingUserCreationForm, MailingUserChangeForm

from config.settings import EMAIL_HOST_USER
from .models import MailingUser


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = MailingUserCreationForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        # user = form.save()
        # self.send_welcome_email(user)
        return super().form_valid(form)

    # TODO реализовать верификацию почты

    # @staticmethod
    # def send_welcome_email(user_data):
    #     user_email = user_data.email
    #
    #     title = "Вы успешно прошли регистрацию!"
    #     message = "И мы вас с этим безумно поздравляем!"
    #     recipient_list = [user_email,]
    #     send_mail(subject=title,
    #               message=message,
    #               from_email=EMAIL_HOST_USER,
    #               recipient_list=recipient_list)


class MailingUserDetailView(LoginRequiredMixin, DetailView):
    template_name = 'users/profile_detail.html'
    model = MailingUser
    context_object_name = 'user'


class MailingProfileTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile_detail.html'


class MailingUserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'users/register.html'
    model = MailingUser
    form_class = MailingUserChangeForm

    def get_success_url(self):
        redirect_pk = self.request.resolver_match.kwargs.get('pk')

        return reverse("users:profile_detail", kwargs={"pk": redirect_pk})
