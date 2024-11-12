class MailingService:

    @staticmethod
    def get_created_mailing(user):
        return user.mailings.filter(status="Создана")

    @staticmethod
    def get_started_mailing(user):
        return user.mailings.filter(status="Запущена")

    @staticmethod
    def get_finished_mailing(user):
        return user.mailings.filter(status="Завершена")
