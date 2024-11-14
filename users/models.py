from django.db import models
from django.contrib.auth.models import AbstractUser


class MailingUser(AbstractUser):

    email = models.EmailField(unique=True, verbose_name="Почта")
    phone_number = models.IntegerField(unique=True, verbose_name="номер телефона")
    avatar = models.ImageField(
        upload_to="users_avatars/", blank=True, null=True, verbose_name="фото профиля"
    )
    country = models.CharField(
        max_length=20,
        verbose_name="страна проживания",
        blank=True,
        null=True,
        default="Неизвестно",
    )

    token = models.CharField(
        max_length=100,
        verbose_name="Токен для подтвержения почты",
        blank=True,
        null=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "phone_number"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}. mail: {self.email}"

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
        permissions = [("can_manage_users", "Управление пользователем")]
