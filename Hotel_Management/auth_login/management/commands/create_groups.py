from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

GROUPS = ["waiter", "manager", "billdesk", "admin"]

class Command(BaseCommand):
    help = "create groups"

    def handle(self, *args, **options):
        for group in GROUPS:
            new_group, created = Group.objects.get_or_create(name = group)

        print("Created default groups")