from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = """
    Добавляет группу менеджеров с необходимой настройкой
    """

    def handle(self, *args, **options):
        can_manage_users = Permission.objects.get(codename='can_manage_users')
        can_manage_clients = Permission.objects.get(codename='can_manage_clients')
        can_manage_message = Permission.objects.get(codename='can_manage_message')
        can_manage_mailing = Permission.objects.get(codename='can_manage_mailing')

        manager_group = Group.objects.create(name='manager')

        manager_group.permissions.add(
            can_manage_users, can_manage_clients, can_manage_message, can_manage_mailing
        )
        manager_group.save()

        print("Группа manager добавлена")



