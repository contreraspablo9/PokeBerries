"""
    Main project urls module
"""
from django.conf import settings

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

from pokeberries.api.views import APIRootView


_patterns = [
    path("admin/", admin.site.urls),
    # todo: web browser urls:
    # path("", include("berries.urls")),
    # redirectin to api/
    path("", RedirectView.as_view(url="api/")),

    # API REST URLS:
    path("api/", APIRootView.as_view(), name="api-root"),
    path("api/berries/", include("berries.api.urls")),
]

# Prepend BASE_PATH
urlpatterns = [
    path(f"{settings.BASE_PATH}", include(_patterns)),
]
