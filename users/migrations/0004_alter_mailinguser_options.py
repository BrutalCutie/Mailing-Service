# Generated by Django 5.1.2 on 2024-11-12 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_mailinguser_country"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="mailinguser",
            options={
                "permissions": [("can_manage_users", "Управление пользователем")],
                "verbose_name": "пользователь",
                "verbose_name_plural": "пользователи",
            },
        ),
    ]