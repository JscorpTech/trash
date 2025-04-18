from rest_framework.permissions import BasePermission
from core.app.choices import RoleChoice


class IsAdminPermission(BasePermission):
    def has_permission(self, request, view):
        return all(
            [
                request.user,
                request.user.is_authenticated,
                request.user.role == RoleChoice.ADMIN,
            ]
        )


class IsSelfPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        # raise Exception(request.user, obj)
        # print(request.user, obj)
        return obj == request.user


class IsOwnerPermission(BasePermission):
    def has_permission(self, request, view):
        return all(
            [
                request.user,
                request.user.is_authenticated,
                request.user.role == RoleChoice.OWNER,
            ]
        )
