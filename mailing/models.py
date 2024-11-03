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
