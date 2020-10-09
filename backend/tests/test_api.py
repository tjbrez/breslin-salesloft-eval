from hamcrest import assert_that, equal_to
from django.test import TestCase
from django.urls import reverse
from unittest.mock import Mock, patch

from .mocks import (
    MockResponse,
    get_mock_people_page_1,
    get_mock_people_page_2,
)


class ApiTests(TestCase):
    @patch("backend.services.requests.get")
    def test_can_get_all_people(self, mock_get):
        mock_get.side_effect = [
            MockResponse(get_mock_people_page_1()),
            MockResponse(get_mock_people_page_2()),
        ]

        response = self.client.get(reverse("api_all_people"))

        assert_that(response.status_code, equal_to(200))
        assert_that(type(response.data), equal_to(list))
        assert_that(len(response.data), equal_to(4))

    @patch("backend.services.requests.get")
    def test_can_get_char_counts(self, mock_get):
        mock_get.side_effect = [
            MockResponse(get_mock_people_page_1()),
            MockResponse(get_mock_people_page_2()),
        ]

        response = self.client.get(reverse("api_char_counts"))

        assert_that(response.status_code, equal_to(200))
        assert_that(type(response.data), equal_to(list))
        assert_that(len(response.data), equal_to(20))
        assert_that(response.data[0]["character"], equal_to("e"))
        assert_that(response.data[0]["count"], equal_to(11))
        assert_that(response.data[19]["character"], equal_to("w"))
        assert_that(response.data[19]["count"], equal_to(1))

    @patch("backend.services.requests.get")
    def test_can_get_duplicates(self, mock_get):
        mock_get.side_effect = [
            MockResponse(get_mock_people_page_1()),
            MockResponse(get_mock_people_page_2()),
        ]

        response = self.client.get(reverse("api_duplicates"))

        assert_that(response.status_code, equal_to(200))
        assert_that(type(response.data), equal_to(list))
        assert_that(len(response.data), equal_to(1))
        assert_that(response.data[0]["person1_id"], equal_to(101694088))
        assert_that(response.data[0]["person2_id"], equal_to(101694090))
