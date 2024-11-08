from mailing.models import Mailing


class MailingService:

    @staticmethod
    def get_sreceivers(mailing_pk):

        mailing = Mailing.objects.get(pk=mailing_pk)
        receivers = mailing.receivers.all()
        names = [x.full_name for x in receivers]

        return ', '.join(names)



