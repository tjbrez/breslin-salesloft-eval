from django.contrib import admin
from django.urls import path

from .views import index, ListPeople, GetEmailCharacterFrequency, ListDuplicatePeople

urlpatterns = [
    # Frontend routes
    path("", index, name="index"),
    path("char-counts", index, name="index"),
    path("duplicate-people", index, name="index"),
    # API routes
    path("api/people", ListPeople.as_view()),
    path("api/people/char-counts", GetEmailCharacterFrequency.as_view()),
    path("api/people/duplicates", ListDuplicatePeople.as_view()),
    # Default Django admin route
    path("admin/", admin.site.urls),
]
