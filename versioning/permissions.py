# 3rd party
from rest_framework.permissions import BasePermission

# Application
from versioning.settings import VERSIONING_API_SECRET


class HasVersioningAPISecret(BasePermission):
    def has_permission(self, request, view) -> bool:
        if not VERSIONING_API_SECRET:
            raise Exception('Environment variable "VERSIONING_API_SECRET" is missing.')
        request_versioning_api_secret = request.META.get("HTTP_VERSIONING_API_SECRET", None)
        return request_versioning_api_secret == VERSIONING_API_SECRET
