import json


class MockResponse:
    def __init__(self, json_data):
        self.json_data = json_data
        self.ok = True

    def json(self):
        return self.json_data


def get_mock_people_page_1():
    # fmt: off
    response = '''
    {
        "metadata": {
            "filtering": {},
            "paging": {
                "per_page": 2,
                "current_page": 1,
                "next_page": 2,
                "prev_page": null,
                "total_pages": 2,
                "total_count": 4
            },
            "sorting": {
                "sort_by": "updated_at",
                "sort_direction": "DESC NULLS LAST"
            }
        },
        "data": [
            {
                "id": 101694088,
                "created_at": "2018-03-13T00:41:41.550510-04:00",
                "updated_at": "2018-03-13T00:41:41.550510-04:00",
                "last_contacted_at": null,
                "last_replied_at": null,
                "first_name": "John",
                "last_name": "Smith",
                "display_name": "John Smith",
                "email_address": "johnsmith@example.com",
                "full_email_address": "'John Smith' <johnsmith@example.com>",
                "secondary_email_address": null,
                "personal_email_address": null,
                "phone": "524-210-5852",
                "phone_extension": null,
                "home_phone": null,
                "mobile_phone": null,
                "linkedin_url": null,
                "title": "National Infrastructure Strategist",
                "city": "East Ashton",
                "state": "Kansas",
                "country": "Albania",
                "work_city": null,
                "work_state": null,
                "work_country": null,
                "crm_url": null,
                "crm_id": null,
                "crm_object_type": null,
                "owner_crm_id": null,
                "person_company_name": null,
                "person_company_website": "http://okongleason.name",
                "person_company_industry": null,
                "do_not_contact": false,
                "bouncing": false,
                "locale": null,
                "personal_website": null,
                "twitter_handle": null,
                "last_contacted_type": null,
                "job_seniority": null,
                "custom_fields": {},
                "tags": [],
                "contact_restrictions": [],
                "counts": {
                    "emails_sent": 0,
                    "emails_viewed": 0,
                    "emails_clicked": 0,
                    "emails_replied_to": 0,
                    "emails_bounced": 0,
                    "calls": 0
                },
                "account": {
                    "_href": "https://api.salesloft.com/v2/accounts/37127834",
                    "id": 37127834
                },
                "owner": {
                    "_href": "https://api.salesloft.com/v2/users/46818",
                    "id": 46818
                },
                "last_contacted_by": null,
                "import": null,
                "person_stage": null
            },
            {
                "id": 101694087,
                "created_at": "2018-03-13T00:41:41.252532-04:00",
                "updated_at": "2018-03-13T00:41:41.252532-04:00",
                "last_contacted_at": null,
                "last_replied_at": null,
                "first_name": "Sue",
                "last_name": "Brown",
                "display_name": "Sue Brown",
                "email_address": "suebroen@example.com",
                "full_email_address": "'Sue Brown' <suebroen@example.com>",
                "secondary_email_address": null,
                "personal_email_address": null,
                "phone": "448.289.9734 x1473",
                "phone_extension": null,
                "home_phone": null,
                "mobile_phone": null,
                "linkedin_url": null,
                "title": "Regional Mobility Engineer",
                "city": "Thomasborough",
                "state": "North Dakota",
                "country": "Cayman Islands",
                "work_city": null,
                "work_state": null,
                "work_country": null,
                "crm_url": null,
                "crm_id": null,
                "crm_object_type": null,
                "owner_crm_id": null,
                "person_company_name": null,
                "person_company_website": "http://boehm.net",
                "person_company_industry": null,
                "do_not_contact": false,
                "bouncing": false,
                "locale": null,
                "personal_website": null,
                "twitter_handle": null,
                "last_contacted_type": null,
                "job_seniority": null,
                "custom_fields": {},
                "tags": [],
                "contact_restrictions": [],
                "counts": {
                    "emails_sent": 0,
                    "emails_viewed": 0,
                    "emails_clicked": 0,
                    "emails_replied_to": 0,
                    "emails_bounced": 0,
                    "calls": 0
                },
                "account": {
                    "_href": "https://api.salesloft.com/v2/accounts/37127835",
                    "id": 37127835
                },
                "owner": {
                    "_href": "https://api.salesloft.com/v2/users/46818",
                    "id": 46818
                },
                "last_contacted_by": null,
                "import": null,
                "person_stage": null
            }
        ]
    }
    '''
    # fmt: on
    return json.loads(response)


def get_mock_people_page_2():
    # fmt: off
    response = '''
    {
        "metadata": {
            "filtering": {},
            "paging": {
                "per_page": 2,
                "current_page": 2,
                "next_page": null,
                "prev_page": 1,
                "total_pages": 2,
                "total_count": 4
            },
            "sorting": {
                "sort_by": "updated_at",
                "sort_direction": "DESC NULLS LAST"
            }
        },
        "data": [
            {
                "id": 101694090,
                "created_at": "2018-03-13T00:41:41.550510-04:00",
                "updated_at": "2018-03-13T00:41:41.550510-04:00",
                "last_contacted_at": null,
                "last_replied_at": null,
                "first_name": "John",
                "last_name": "Smith",
                "display_name": "John Smith",
                "email_address": "johnsmitth@example.com",
                "full_email_address": "'John Smith' <johnsmitth@example.com>",
                "secondary_email_address": null,
                "personal_email_address": null,
                "phone": "524-210-5854",
                "phone_extension": null,
                "home_phone": null,
                "mobile_phone": null,
                "linkedin_url": null,
                "title": "National Infrastructure Strategist",
                "city": "East Ashton",
                "state": "Kansas",
                "country": "Albania",
                "work_city": null,
                "work_state": null,
                "work_country": null,
                "crm_url": null,
                "crm_id": null,
                "crm_object_type": null,
                "owner_crm_id": null,
                "person_company_name": null,
                "person_company_website": "http://okongleason.name",
                "person_company_industry": null,
                "do_not_contact": false,
                "bouncing": false,
                "locale": null,
                "personal_website": null,
                "twitter_handle": null,
                "last_contacted_type": null,
                "job_seniority": null,
                "custom_fields": {},
                "tags": [],
                "contact_restrictions": [],
                "counts": {
                    "emails_sent": 0,
                    "emails_viewed": 0,
                    "emails_clicked": 0,
                    "emails_replied_to": 0,
                    "emails_bounced": 0,
                    "calls": 0
                },
                "account": {
                    "_href": "https://api.salesloft.com/v2/accounts/37127834",
                    "id": 37127834
                },
                "owner": {
                    "_href": "https://api.salesloft.com/v2/users/46818",
                    "id": 46818
                },
                "last_contacted_by": null,
                "import": null,
                "person_stage": null
            },
            {
                "id": 101694083,
                "created_at": "2018-03-13T00:41:41.252532-04:00",
                "updated_at": "2018-03-13T00:41:41.252532-04:00",
                "last_contacted_at": null,
                "last_replied_at": null,
                "first_name": "Jill",
                "last_name": "White",
                "display_name": "Jill White",
                "email_address": "jillwhite@example.com",
                "full_email_address": "'Jill White' <jillwhite@example.com>",
                "secondary_email_address": null,
                "personal_email_address": null,
                "phone": "448.289.9732 x1473",
                "phone_extension": null,
                "home_phone": null,
                "mobile_phone": null,
                "linkedin_url": null,
                "title": "Regional Mobility Engineer",
                "city": "Thomasborough",
                "state": "North Dakota",
                "country": "Cayman Islands",
                "work_city": null,
                "work_state": null,
                "work_country": null,
                "crm_url": null,
                "crm_id": null,
                "crm_object_type": null,
                "owner_crm_id": null,
                "person_company_name": null,
                "person_company_website": "http://boehm.net",
                "person_company_industry": null,
                "do_not_contact": false,
                "bouncing": false,
                "locale": null,
                "personal_website": null,
                "twitter_handle": null,
                "last_contacted_type": null,
                "job_seniority": null,
                "custom_fields": {},
                "tags": [],
                "contact_restrictions": [],
                "counts": {
                    "emails_sent": 0,
                    "emails_viewed": 0,
                    "emails_clicked": 0,
                    "emails_replied_to": 0,
                    "emails_bounced": 0,
                    "calls": 0
                },
                "account": {
                    "_href": "https://api.salesloft.com/v2/accounts/37127835",
                    "id": 37127835
                },
                "owner": {
                    "_href": "https://api.salesloft.com/v2/users/46818",
                    "id": 46818
                },
                "last_contacted_by": null,
                "import": null,
                "person_stage": null
            }
        ]
    }
    '''
    # fmt: on
    return json.loads(response)
