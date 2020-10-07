import environ
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


def get_email_character_frequency_counts():
    character_counts = {}
    all_people = get_all_people_from_sl_api()

    # Loop all charcters in all email addresses and add to count dictionary
    for person in all_people:
        for char in person["email_address"]:
            if char in character_counts:
                character_counts[char] += 1
            else:
                character_counts[char] = 1

    # Sort completed dictionary by decending count
    character_counts = {k: v for k, v in sorted(character_counts.items(), key=lambda item: item[1], reverse=True)}

    return character_counts


def get_duplicate_people():
    duplicate_records = []
    all_people = get_all_people_from_sl_api()

    # Loop all people and compare email using a fuzzywuzzy partial ratio comparison
    for person in all_people:
        for other_person in all_people:
            email_ratio = fuzz.partial_ratio(person["email_address"].lower(), other_person["email_address"].lower())
            name_ratio = fuzz.partial_ratio(person["display_name"].lower(), other_person["display_name"].lower())
            if (email_ratio >= 90 or name_ratio >= 95) and person["id"] != other_person["id"]:

                duplicate_id = (
                    str(max(person["id"], other_person["id"])) + "_" + str(min(person["id"], other_person["id"]))
                )

                # Check to see if Duplicate is already in the array and skip if it is
                if next(
                    (dup for dup in duplicate_records if dup["duplicate_id"] == duplicate_id),
                    False,
                ):
                    continue

                # Add Duplicate dict to array
                duplicate_records.append(
                    {
                        "duplicate_id": duplicate_id,
                        "person1_id": person["id"],
                        "person1_name": person["display_name"],
                        "person1_email": person["email_address"],
                        "person2_id": other_person["id"],
                        "person2_name": other_person["display_name"],
                        "person2_email": other_person["email_address"],
                        "email_ratio": email_ratio,
                        "name_ratio": name_ratio,
                    }
                )

    return duplicate_records
