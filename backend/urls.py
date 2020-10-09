from django.contrib import admin
from django.urls import path

from .views import index, ListPeople, GetEmailCharacterFrequency, ListDuplicatePeople

urlpatterns = [
    # Frontend routes
    path("", index, name="index"),
    path("char-counts", index, name="char-counts"),
    path("duplicate-people", index, name="duplicate-people"),
    path("enterprise-ready", index, name="enterprise-ready"),
    # API routes
    path("api/people", ListPeople.as_view(), name="api_all_people"),
    path("api/people/char-counts", GetEmailCharacterFrequency.as_view(), name="api_char_counts"),
    path("api/people/duplicates", ListDuplicatePeople.as_view(), name="api_duplicates"),
    # Default Django admin route
    path("admin/", admin.site.urls),
]
