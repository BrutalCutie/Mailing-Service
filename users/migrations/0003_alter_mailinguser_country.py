# Generated by Django 5.1.2 on 2024-11-04 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_mailinguser_country_mailinguser_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailinguser',
            name='country',
            field=models.CharField(blank=True, default='Неизвестно', max_length=20, null=True, verbose_name='страна проживания'),
        ),
    ]