import base64
from urllib.parse import urlencode
import requests
import api
import pytest


def sso_token():
    print('sso')
    token_url = 'https://adfsonekey-auth.login.sys.uat.cf.az.cihs.gov.on.ca/oauth/token'
    username = '53c40844-99ca-4147-8719-78efa536bcf4'
    password = '22438e67-77cf-40ed-957e-28a261c82fe0'
    headers = {
        'Authorization': f'Basic {base64.b64encode(f"{username}:{password}".encode()).decode()}',
        'Content-Type': 'application/x-www-form-urlencoded',  # Adjust the content type based on your API's requirements
    }
    data = {
        'grant_type': 'client_credentials'
    }
    # Encode the data in x-www-form-urlencoded format
    encoded_data = urlencode(data)

    # Make the API request
    response = requests.post(token_url, data=encoded_data, headers=headers)
    print(response.status_code)  # 204
    print(response.text)
    response_json = response.json()
    access_token = response_json.get('access_token')
    print(access_token)
    return response.text

# sso_token()

# DELETE - online offering - https://netsdc.visualstudio.com/SDC/_workitems/edit/98391
# You must review the db to ensure your entities deleted (the Course, ElectronicAddressOwnership, & ElectronicAddress)
def api_01_delete_online_offering():
    print('api_01_delete_online_offering')
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/ClassOffering/ABA44D61-9840-4E77-B2CE-A73334771CA4"  # YOUR OFFERING ID HERE
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIxMzE5MjRiMzFmZWQ0ZWVjOWE4MzUyY2Q4MTVkNDY5ZCIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDA0OTExODgsImV4cCI6MTcwMDUzNDM4OCwiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.YuYXSrLX5tUUgBPyCQ-b9N2kFGVK4vtpOofTNUMTzdcULxUzGWn9OXbeCM9szBsHG1-VH1AgPbP9t5Qs03ep1P27F5QEw3O0E3DeCacFVF-UA4CuFQDRlnsIV88s9rTOkf7pfpnTJt7ODc92c2u5RNNnaam1Vod0CN85UvXZ2B5zZSmRwEVysTXhUfihizQ5nN-25-iVgftBJ9gpWmPz6qQwiet5_iCYhbn8q6XI4w3DwdzuLCByPOFTvnsuQLJoeAYGWGCqcqspxSS2MIABcuLJHzBg2SJG-I0LJvn3bwWxaRQ6BZcSiDM2Vq-0Vsp1RaVEMlEyEMKwWSIoHm6CyQ",
        "key": "E933D1B3-3404-4EB5-A70F-B2128B3A2C6A",
        "Content-Type": "application/json; charset=utf-8"
    }
    response = requests.delete(url, headers=headers)
    print(response.status_code)  # 204
    print(response.text)  # print(response.json())
    return response.text


# ADD - online offering - https://netsdc.visualstudio.com/SDC/_workitems/edit/98383
def api_03_add_online_offering():
    print('03_add_online_offering')
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/OnlineOffering"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI4YjJlYzg1ZTUyOTM0ZTk4YTcyMmJhZWYxMDUyMTlmYyIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDA1ODczNjMsImV4cCI6MTcwMDYzMDU2MywiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.RyrTQxYE_0ayvy3vFv5gA7ebim-x-HqUtUh1VOrA448Yv785qRqJuEb38LnsjigF8wmbetPI8vJkyM2rQ48fP3iZddOIunDDvPJ4IdJpEq1zzIUKecCzu3yn1rm7QzaQuKIWBd_Vo2o30i3sibUQ0epztFHyXctv5Ct_Xxj8V0W0dm4O4yKn-JdQsfDF6jOe5TMxYoeWeRIYTxi-EoX4swWVXiOghdXEnPsUD-Cksua4vVVq7j-4L1Nw4FuEnGJ5o0aTmbYIMnDpaXu5OmTponTlPzIvESzF0VPYeg4PbVum3mEtUDJjzeceFysb73NWVwWyk66mZ9ZdMgs5wCcVFw",
        "key": "E933D1B3-3404-4EB5-A70F-B2128B3A2C6A",
        "Content-Type": "application/json"
    }
    body = {
      "offeringId": "wah-132",
      "trainingStandardKey": "WAH-E-B-O",
      "courseName": "Working At Heights",
      "price": 250,
      "courseDuration": 3,
      "externalRegistrationUrl": "https://trainingproviderreservationsystem/register"
    }
    response = requests.post(url, json=body, headers=headers)
    print(response.status_code)  # 204
    print(response.text)  # print(response.json())
    return response.text

api_03_add_online_offering()



