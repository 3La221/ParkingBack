from rest_framework.permissions import BasePermission

class IsVerificateur(BasePermission):
    message = "You are not a verificateur"
    def has_permission(self, request, view):
        return hasattr(request.user, "verificateur")