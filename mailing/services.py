from mailing.models import Mailing


class MailingService:

    @staticmethod
    def get_created_mailing(user, show_all=False):
        if show_all:
            return Mailing.objects.filter(status="Создана")
        return user.mailings.filter(status="Создана")

    @staticmethod
    def get_started_mailing(user, show_all=False):
        if show_all:
            return Mailing.objects.filter(status="Запущена")
        return user.mailings.filter(status="Запущена")

    @staticmethod
    def get_finished_mailing(user, show_all=False):
        if show_all:
            return Mailing.objects.filter(status="Завершена")
        return user.mailings.filter(status="Завершена")
