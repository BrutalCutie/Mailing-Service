from django.db import models


class Receiver(models.Model):

    email = models.EmailField(unique=True, null=False, blank=False, verbose_name="почта получателя")
    full_name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Ф.И.О.")
    commentary = models.TextField(verbose_name="Комментарий о получателе рассылки")

    def __str__(self):
        return f"{self.full_name} | {self.email}"

    class Meta:
        verbose_name = 'Получатель рассылки'
        verbose_name_plural = 'Получатели рассылки'
        # permissions = [()]


class Message(models.Model):
    subject = models.CharField(max_length=100, blank=False, null=False, verbose_name="тема сообщения")
    message_text = models.TextField(verbose_name="текст сообщения")

    def __str__(self):
        max_length = 20
        is_long = len(self.subject.__str__()) > max_length
        add_symb = ''
        if is_long:
            add_symb = '...'

        return f"{self.pk} | {self.subject[:max_length]}{add_symb}"

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        # permissions = [()]


class Mailing(models.Model):
    # TODO проверить как будет со списком строк, а не списком кортежей строк
    STATUS_CHOICES = [
        ("Завершена", "Завершена"),
        ("Создана", "Создана"),
        ("Запущена", "Запущена"),
    ]

    mailing_start_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время первой отправки")
    mailing_end_at = models.DateTimeField(verbose_name="Дата и время окончания  отправки")
    status = models.CharField(choices=STATUS_CHOICES, verbose_name='Статус')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='mailings', verbose_name='Сообщение')
    receivers = models.ManyToManyField(Receiver, 'receivers', verbose_name='Получатели')

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"


class MailingAttempt(models.Model):
    STATUS_CHOICES = [
        ("Успешно", "Успешно"),
        ("Не успешно", "Не успешно"),
    ]

    attempt_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время попытки")
    status = models.CharField(choices=STATUS_CHOICES, verbose_name='Статус')
    server_response = models.TextField(verbose_name="Ответ почтового сервера")
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name="Рассылка")

    class Meta:
        verbose_name = "Попытка рассылки"
        verbose_name_plural = "Попытки рассылки"
