import json
import requests

from django.test import TestCase
from hamcrest import assert_that, not_none, equal_to
from unittest.mock import Mock, patch

from ..services import (
    get_page_of_people_from_sl_api,
    get_all_people_from_sl_api,
    get_email_character_frequency_counts,
    get_duplicate_people,
)

from .mocks import (
    MockResponse,
    get_mock_people_page_1,
    get_mock_people_page_2,
)


class ServiceTests(TestCase):
    @patch("backend.services.requests.get")
    def test_can_get_page_of_people_from_sl_api(self, mock_get):
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = get_mock_people_page_1()

        response = get_page_of_people_from_sl_api(1)

        assert_that(response.ok, equal_to(True))
        assert_that(response.json(), not_none)
        assert_that(len(response.json()["data"]), equal_to(2))

    @patch("backend.services.requests.get")
    def test_can_get_all_people_from_sl_api(self, mock_get):
        mock_get.side_effect = [
            MockResponse(get_mock_people_page_1()),
            MockResponse(get_mock_people_page_2()),
        ]

        response = get_all_people_from_sl_api()

        assert_that(type(response), equal_to(list))
        assert_that(len(response), equal_to(4))

    @patch("backend.services.requests.get")
    def test_can_get_email_character_count(self, mock_get):
        mock_get.side_effect = [
            MockResponse(get_mock_people_page_1()),
            MockResponse(get_mock_people_page_2()),
        ]

        response = get_email_character_frequency_counts()

        assert_that(type(response), equal_to(list))
        assert_that(len(response), equal_to(20))
        assert_that(response[0]["character"], equal_to("e"))
        assert_that(response[0]["count"], equal_to(11))
        assert_that(response[19]["character"], equal_to("w"))
        assert_that(response[19]["count"], equal_to(1))

    @patch("backend.services.requests.get")
    def test_can_get_duplicate_people(self, mock_get):
        mock_get.side_effect = [
            MockResponse(get_mock_people_page_1()),
            MockResponse(get_mock_people_page_2()),
        ]

        response = get_duplicate_people()

        assert_that(type(response), equal_to(list))
        assert_that(len(response), equal_to(1))
        assert_that(response[0]["person1_id"], equal_to(101694088))
        assert_that(response[0]["person2_id"], equal_to(101694090))
