from django.db import models
from users.models import MailingUser


class Receiver(models.Model):
    email = models.EmailField(
        unique=True, null=False, blank=False, verbose_name="почта получателя"
    )
    full_name = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Ф.И.О."
    )
    commentary = models.TextField(verbose_name="Комментарий о получателе рассылки")
    owner = models.ForeignKey(
        MailingUser,
        on_delete=models.CASCADE,
        related_name="receivers",
        verbose_name="Владелец модели получателя",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.full_name} | {self.email}"

    class Meta:
        verbose_name = "Получатель рассылки"
        verbose_name_plural = "Получатели рассылки"
        permissions = [("can_manage_clients", "Управление клиентами")]


class Message(models.Model):
    subject = models.CharField(
        max_length=100, blank=False, null=False, verbose_name="тема сообщения"
    )
    message_text = models.TextField(verbose_name="текст сообщения")
    owner = models.ForeignKey(
        MailingUser,
        on_delete=models.CASCADE,
        related_name="messages",
        verbose_name="Владелец модели сообщения",
        null=True,
        blank=True,
    )

    def __str__(self):
        max_length = 20
        is_long = len(self.subject.__str__()) > max_length
        add_symb = ""
        if is_long:
            add_symb = "..."

        return f"{self.pk} | {self.subject[:max_length]}{add_symb}"

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        permissions = [("can_manage_message", "Управление сообщениями")]


class Mailing(models.Model):
    STATUS_CHOICES = [
        ("Завершена", "Завершена"),
        ("Создана", "Создана"),
        ("Запущена", "Запущена"),
    ]

    mailing_start_at = models.DateTimeField(
        verbose_name="дата и время первой отправки", null=True, blank=True
    )
    mailing_end_at = models.DateTimeField(
        verbose_name="дата и время окончания  отправки", null=True, blank=True
    )
    status = models.CharField(
        choices=STATUS_CHOICES, verbose_name="статус", default="Создана"
    )
    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        related_name="mailings",
        verbose_name="сообщение",
    )
    receivers = models.ManyToManyField(Receiver, "receivers", verbose_name="получатели")
    owner = models.ForeignKey(
        MailingUser,
        on_delete=models.CASCADE,
        related_name="mailings",
        verbose_name="Владелец модели рассылки",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.pk} | {self.owner} | {self.status}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        permissions = [("can_manage_mailing", "Управление рассылкой")]


class MailingAttempt(models.Model):
    STATUS_CHOICES = [("Успешно", "Успешно"), ("Не успешно", "Не успешно")]

    attempt_at = models.DateTimeField(
        auto_now_add=True, verbose_name="дата и время попытки"
    )
    status = models.CharField(choices=STATUS_CHOICES, verbose_name="статус")
    server_response = models.TextField(verbose_name="ответ почтового сервера")
    mailing = models.ForeignKey(
        Mailing, on_delete=models.CASCADE, verbose_name="рассылка"
    )

    def __str__(self):
        return f"{self.pk} | {self.status}"

    class Meta:
        verbose_name = "Попытка рассылки"
        verbose_name_plural = "Попытки рассылки"
