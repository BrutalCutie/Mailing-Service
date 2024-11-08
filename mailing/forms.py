from django.forms import ModelForm
from mailing.models import Mailing, Message, Receiver


class MailingForm(ModelForm):
    class Meta:
        model = Mailing
        fields = ["receivers", "message", "mailing_start_at"]
