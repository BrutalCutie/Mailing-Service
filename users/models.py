from django.db import models
from django.contrib.auth.models import AbstractUser


class MailingUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone_number = models.IntegerField(unique=True, verbose_name="номер телефона")
    avatar = models.ImageField(upload_to='users_avatars/', blank=True, null=True, verbose_name='фото профиля')
    country = models.CharField(max_length=20, verbose_name='страна проживания', blank=False, null=False, default='Неизвестно')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.first_name} {self.last_name}. mail: {self.email}"
