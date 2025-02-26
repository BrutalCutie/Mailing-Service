# Generated by Django 5.1.2 on 2024-11-04 04:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Mailing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "mailing_start_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата и время первой отправки"
                    ),
                ),
                (
                    "mailing_end_at",
                    models.DateTimeField(
                        verbose_name="дата и время окончания  отправки"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Завершена", "Завершена"),
                            ("Создана", "Создана"),
                            ("Запущена", "Запущена"),
                        ],
                        verbose_name="статус",
                    ),
                ),
            ],
            options={
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
                "permissions": [("can_manage_mailing", "Управление рассылкой")],
            },
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "subject",
                    models.CharField(max_length=100, verbose_name="тема сообщения"),
                ),
                ("message_text", models.TextField(verbose_name="текст сообщения")),
            ],
            options={
                "verbose_name": "Сообщение",
                "verbose_name_plural": "Сообщения",
                "permissions": [("can_manage_message", "Управление сообщениями")],
            },
        ),
        migrations.CreateModel(
            name="Receiver",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="почта получателя"
                    ),
                ),
                ("full_name", models.CharField(max_length=100, verbose_name="Ф.И.О.")),
                (
                    "commentary",
                    models.TextField(verbose_name="Комментарий о получателе рассылки"),
                ),
            ],
            options={
                "verbose_name": "Получатель рассылки",
                "verbose_name_plural": "Получатели рассылки",
                "permissions": [("can_manage_clients", "Управление клиентами")],
            },
        ),
        migrations.CreateModel(
            name="MailingAttempt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "attempt_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата и время попытки"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("Успешно", "Успешно"), ("Не успешно", "Не успешно")],
                        verbose_name="статус",
                    ),
                ),
                (
                    "server_response",
                    models.TextField(verbose_name="ответ почтового сервера"),
                ),
                (
                    "mailing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mailing.mailing",
                        verbose_name="рассылка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Попытка рассылки",
                "verbose_name_plural": "Попытки рассылки",
            },
        ),
        migrations.AddField(
            model_name="mailing",
            name="message",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="mailings",
                to="mailing.message",
                verbose_name="сообщение",
            ),
        ),
        migrations.AddField(
            model_name="mailing",
            name="receivers",
            field=models.ManyToManyField(
                related_name="receivers",
                to="mailing.receiver",
                verbose_name="получатели",
            ),
        ),
    ]
