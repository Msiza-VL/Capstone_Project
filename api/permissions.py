from rest_framework.permissions import SAFE_METHODS, BasePermission

class IsAuthenticatedOrCreate(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.method == 'POST':
            return True
        return request.user.is_authenticated