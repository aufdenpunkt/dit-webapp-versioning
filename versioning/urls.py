# Django
from django.urls.conf import path
from django.views.decorators.cache import never_cache

# 3rd party
from rest_framework.urlpatterns import format_suffix_patterns

# Application
from versioning.views import CurrentWebAppVersionView, WebAppVersionCreateView

app_name = "versioning"

urlpatterns = [
    path("versioning/api/web-app-version", WebAppVersionCreateView.as_view()),
    path("versioning/api/web-app-version/current", never_cache(CurrentWebAppVersionView.as_view())),
]

urlpatterns = format_suffix_patterns(urlpatterns)
