from django.forms import ModelForm
from mailing.models import Mailing, Message, Receiver


class MailingForm(ModelForm):
    class Meta:
        model = Mailing
        fields = ["receivers", "message"]


class ReceiverForm(ModelForm):
    class Meta:
        model = Receiver
        fields = ["email", "full_name", "commentary"]
