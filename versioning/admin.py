from typing import Dict, Optional

# Django
from django.contrib import admin
from django.http.request import HttpRequest
from django.template.response import TemplateResponse

# Application
from versioning.models import WebAppVersion


@admin.register(WebAppVersion)
class WebAppVersionAdmin(admin.ModelAdmin):
    list_display = [
        "version_number",
        "in_stores",
    ]

    list_filter = [
        "in_stores",
    ]

    search_fields = [
        "version_number",
    ]

    sortable_by = [
        "version_number",
    ]

    list_editable = [
        "in_stores",
    ]

    def changelist_view(
        self, request: HttpRequest, extra_context: Optional[Dict[str, str]] = None
    ) -> TemplateResponse:
        extra_context = extra_context or {}
        try:
            extra_context["current_version"] = WebAppVersion.objects.get(in_stores=True)
        except WebAppVersion.DoesNotExist:
            pass
        return super().changelist_view(request, extra_context=extra_context)
