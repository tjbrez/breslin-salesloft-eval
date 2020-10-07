from django.contrib import admin
from django.urls import path

from .views import index, ListPeople, GetEmailCharacterFrequency, ListDuplicatePeople

urlpatterns = [
    path("", index, name="index"),
    path("api/people", ListPeople.as_view()),
    path("api/people/email-char-frequency", GetEmailCharacterFrequency.as_view()),
    path("api/people/duplicates", ListDuplicatePeople.as_view()),
    path("admin/", admin.site.urls),
]
