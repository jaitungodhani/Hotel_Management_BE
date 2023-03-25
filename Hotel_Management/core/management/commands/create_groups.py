from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group
GROUPS = ['Waiter', 'Manager', 'Bill Desk', 'Admin']

class Command(BaseCommand):

    help = 'Creates Groups'

    def handle(self, *args, **options):
        for group in GROUPS:
            try:
                new_group, created = Group.objects.get_or_create(name = group)
            except Exception as e:
                raise CommandError(str(e))

        print("Created default groups")
        