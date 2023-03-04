from django.contrib.auth.models import Group
from rest_framework import permissions


def _is_in_group(user, group):
    try:
        return Group.objects.get(name=group).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return None

def _has_group_permission(user, required_groups):
    return any(_is_in_group(user, group) for group in required_groups)


class IsAdmin(permissions.BasePermission):
    required_groups = ['admin']

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and has_group_permission