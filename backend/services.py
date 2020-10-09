import environ
import itertools
import requests

from fuzzywuzzy import fuzz


def get_page_of_people_from_sl_api(page):
    # Get URL and API Key from env variables
    env = environ.Env(
        SL_API_PEOPLE_URL=(str, ""),
        SL_API_KEY=(str, ""),
    )
    environ.Env.read_env()

    # Make call to SalesLoft API and store response
    response = requests.get(
        env("SL_API_PEOPLE_URL") + "?per_page=100&include_paging_counts=true&page=" + str(page),
        headers={"Authorization": "Bearer " + env("SL_API_KEY")},
    )
    return response


def get_all_people_from_sl_api():
    # Get first page of People results
    response = get_page_of_people_from_sl_api(1)

    # TODO: Improve error handling when response is not as expected
    if not response.ok:
        return []

    all_people = response.json()["data"]
    next_page = 2

    # Loop through remaining pages and concatenate results into single list of People
    while next_page <= response.json()["metadata"]["paging"]["total_pages"]:
        all_people = all_people + get_page_of_people_from_sl_api(str(next_page)).json()["data"]
        next_page = next_page + 1
    return all_people


def add_character_to_list(character_counts, char):
    # Helper function to manage and add to character count list
    exists = False
    for item in character_counts:
        if item["character"] == char:
            item["count"] = item["count"] + 1
            exists = True

    if exists == False:
        character_counts.append({"character": char, "count": 1})

    return character_counts


def get_email_character_frequency_counts():
    character_counts = []
    all_people = get_all_people_from_sl_api()

    # Loop all charcters in all email addresses and add to count
    for person in all_people:
        for char in person["email_address"]:
            character_counts = add_character_to_list(character_counts, char)

    # Sort completed lest by decending count
    character_counts = sorted(character_counts, key=lambda i: i["count"], reverse=True)

    return character_counts


def get_duplicate_people():
    duplicate_records = []
    all_people = get_all_people_from_sl_api()

    # Iterate all people and compare email using a fuzzywuzzy partial ratio comparison
    for person, other_person in itertools.combinations(all_people, 2):
        email_ratio = fuzz.partial_ratio(person["email_address"].lower(), other_person["email_address"].lower())
        if email_ratio >= 90:

            # Add Duplicate dict to array
            duplicate_records.append(
                {
                    "person1_id": person["id"],
                    "person1_name": person["display_name"],
                    "person1_email": person["email_address"],
                    "person2_id": other_person["id"],
                    "person2_name": other_person["display_name"],
                    "person2_email": other_person["email_address"],
                    "email_ratio": email_ratio,
                }
            )

    return duplicate_records
