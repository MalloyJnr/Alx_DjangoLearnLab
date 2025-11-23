# app_name/management/commands/create_groups.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = "Create default groups and assign permissions"

    def handle(self, *args, **kwargs):
        # Create groups
        viewers, _ = Group.objects.get_or_create(name="Viewers")
        editors, _ = Group.objects.get_or_create(name="Editors")
        admins, _ = Group.objects.get_or_create(name="Admins")

        # Fetch permissions
        perms = Permission.objects.filter(codename__in=[
            "can_view", "can_create", "can_edit", "can_delete"
        ])

        # Assign permissions to groups
        view_only = perms.filter(codename="can_view")
        full_access = perms  # all permissions

        viewers.permissions.set(view_only)
        editors.permissions.set(perms.filter(codename__in=["can_view", "can_create", "can_edit"]))
        admins.permissions.set(full_access)

        self.stdout.write(self.style.SUCCESS("Groups and permissions created successfully!"))
