from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache

from rest_framework.views import APIView
from rest_framework.response import Response

from .services import (
    get_all_people_from_sl_api,
    get_email_character_frequency_counts,
    get_duplicate_people,
)

# Serve Single Page Application
index = never_cache(TemplateView.as_view(template_name="index.html"))


class ListPeople(APIView):
    """
    View to list all People records that are available via the SalesLoft API.
    """

    def get(self, request, format=None):
        """
        Returns a list of all People records.
        """
        return Response(get_all_people_from_sl_api())


class GetEmailCharacterFrequency(APIView):
    """
    View to return frequency count of all the unique characters in all the email addresses of
    all the People from the SalesLoft API, sorted by frequency count.
    """

    def get(self, request, format=None):
        """
        Returns a list of email character counts, sorted by frequency.
        """
        return Response(get_email_character_frequency_counts())


class ListDuplicatePeople(APIView):
    """
    View to return a list of People records that are possible duplicates.
    """

    def get(self, request, format=None):
        """
        Returns a list of Duplicate records
        """
        return Response(get_duplicate_people())