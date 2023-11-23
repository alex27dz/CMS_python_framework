import base64
from urllib.parse import urlencode
import requests
import api
import pytest
import time


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
def api_01_delete_online_offering():
    print('api_01_delete_online_offering')
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/OnlineOffering/wah-131"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIyYjU3MjNlNTEyN2I0Zjc1YTI5NDMxYzBkYTM0YTUyNSIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDA3NTE2MDMsImV4cCI6MTcwMDc5NDgwMywiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.Zxa_3Th3MtTuPjReHZkLen8ja-k2Pr5-KhZCQ2ri2CSzRXprVykKoJRjIdpST6PCKEzoOsgO-0EICChzrXpJ5ooxNjg9digwsjuGOlMzdJqHIss1328edhdvbxCTZ5gSCGaOSLD03aCxJrdV9vkr5yk5Lf04UQuPHwIxjfJ3gtNOtLJA5xUq5LdQWfks0RuEb2DNg6v8CIqvC7jqeljkhb2OoNb0gyaSKhsALHxd9oD1KykinK2J2rMQ9Z9pzIigRRTL4R0YqyrwZamaFzw3v-0D7buTDlVUsh62dx_27ebk0PcyR_wL_QUnbKOgWa8YlfE18lpxwgZHte22pV5KPQ",
        "key": "E933D1B3-3404-4EB5-A70F-B2128B3A2C6A",
        "Content-Type": "application/json; charset=utf-8"
    }
    response = requests.delete(url, headers=headers)
    print(response.status_code)  # 204
    print(response.text)  # print(response.json())
    return response.text
def api_02_update_online_offering():
    print('02_update_online_offerings')
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/OnlineOffering/wah-133"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIyYjU3MjNlNTEyN2I0Zjc1YTI5NDMxYzBkYTM0YTUyNSIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDA3NTE2MDMsImV4cCI6MTcwMDc5NDgwMywiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.Zxa_3Th3MtTuPjReHZkLen8ja-k2Pr5-KhZCQ2ri2CSzRXprVykKoJRjIdpST6PCKEzoOsgO-0EICChzrXpJ5ooxNjg9digwsjuGOlMzdJqHIss1328edhdvbxCTZ5gSCGaOSLD03aCxJrdV9vkr5yk5Lf04UQuPHwIxjfJ3gtNOtLJA5xUq5LdQWfks0RuEb2DNg6v8CIqvC7jqeljkhb2OoNb0gyaSKhsALHxd9oD1KykinK2J2rMQ9Z9pzIigRRTL4R0YqyrwZamaFzw3v-0D7buTDlVUsh62dx_27ebk0PcyR_wL_QUnbKOgWa8YlfE18lpxwgZHte22pV5KPQ",
        "key": "E933D1B3-3404-4EB5-A70F-B2128B3A2C6A",
        "Content-Type": "application/json"
    }
    body = {
      "courseName": "JHSC - Part One",
      "price": 222,
      "courseDuration": 3,
      "externalRegistrationUrl": "https://trainingproviderreservationsystem/register"
    }
    response = requests.patch(url, json=body, headers=headers)
    print(response.status_code)  # 204
    print(response.text)  # print(response.json())
    return response.text
def api_03_add_online_offering():
    print('03_add_online_offering')
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/OnlineOffering"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIyYjU3MjNlNTEyN2I0Zjc1YTI5NDMxYzBkYTM0YTUyNSIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDA3NTE2MDMsImV4cCI6MTcwMDc5NDgwMywiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.Zxa_3Th3MtTuPjReHZkLen8ja-k2Pr5-KhZCQ2ri2CSzRXprVykKoJRjIdpST6PCKEzoOsgO-0EICChzrXpJ5ooxNjg9digwsjuGOlMzdJqHIss1328edhdvbxCTZ5gSCGaOSLD03aCxJrdV9vkr5yk5Lf04UQuPHwIxjfJ3gtNOtLJA5xUq5LdQWfks0RuEb2DNg6v8CIqvC7jqeljkhb2OoNb0gyaSKhsALHxd9oD1KykinK2J2rMQ9Z9pzIigRRTL4R0YqyrwZamaFzw3v-0D7buTDlVUsh62dx_27ebk0PcyR_wL_QUnbKOgWa8YlfE18lpxwgZHte22pV5KPQ",
        "key": "E933D1B3-3404-4EB5-A70F-B2128B3A2C6A",
        "Content-Type": "application/json"
    }
    body = {
      "offeringId": "wah-131",    # need to make a new ID any new call
      "trainingStandardKey": "JHSC-2014-1-10171",  # related to the Class ID inside the training programs schedules
      "courseName": "JHSC - Part One",
      "price": 111,
      "courseDuration": 4,
      "externalRegistrationUrl": "https://trainingproviderreservationsystem/register"
    }
    response = requests.post(url, json=body, headers=headers)
    print(response.status_code)  # 204
    print(response.text)  # print(response.json())
    return response.text
def api_04_delete_class_offering():
    print('04_delete_class_offerings')
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/ClassOffering/wah-381"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIyYjU3MjNlNTEyN2I0Zjc1YTI5NDMxYzBkYTM0YTUyNSIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDA3NTE2MDMsImV4cCI6MTcwMDc5NDgwMywiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.Zxa_3Th3MtTuPjReHZkLen8ja-k2Pr5-KhZCQ2ri2CSzRXprVykKoJRjIdpST6PCKEzoOsgO-0EICChzrXpJ5ooxNjg9digwsjuGOlMzdJqHIss1328edhdvbxCTZ5gSCGaOSLD03aCxJrdV9vkr5yk5Lf04UQuPHwIxjfJ3gtNOtLJA5xUq5LdQWfks0RuEb2DNg6v8CIqvC7jqeljkhb2OoNb0gyaSKhsALHxd9oD1KykinK2J2rMQ9Z9pzIigRRTL4R0YqyrwZamaFzw3v-0D7buTDlVUsh62dx_27ebk0PcyR_wL_QUnbKOgWa8YlfE18lpxwgZHte22pV5KPQ",
        "key": "E933D1B3-3404-4EB5-A70F-B2128B3A2C6A",
        "Content-Type": "application/json; charset=utf-8"
    }

    response = requests.delete(url, headers=headers)
    print(response.status_code)  # 204
    print(response.text)  # print(response.json())
    return response.text
def api_05_update_class_offering():
    print('05_update_class_offerings')
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/ClassOffering/wah-381"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIyYjU3MjNlNTEyN2I0Zjc1YTI5NDMxYzBkYTM0YTUyNSIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDA3NTE2MDMsImV4cCI6MTcwMDc5NDgwMywiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.Zxa_3Th3MtTuPjReHZkLen8ja-k2Pr5-KhZCQ2ri2CSzRXprVykKoJRjIdpST6PCKEzoOsgO-0EICChzrXpJ5ooxNjg9digwsjuGOlMzdJqHIss1328edhdvbxCTZ5gSCGaOSLD03aCxJrdV9vkr5yk5Lf04UQuPHwIxjfJ3gtNOtLJA5xUq5LdQWfks0RuEb2DNg6v8CIqvC7jqeljkhb2OoNb0gyaSKhsALHxd9oD1KykinK2J2rMQ9Z9pzIigRRTL4R0YqyrwZamaFzw3v-0D7buTDlVUsh62dx_27ebk0PcyR_wL_QUnbKOgWa8YlfE18lpxwgZHte22pV5KPQ",
        "key": "E933D1B3-3404-4EB5-A70F-B2128B3A2C6A",
        "Content-Type": "application/json"
    }
    body = {
      "courseName": "Working At Heights",
      "seatsRemaining": 15,
      "contactForPricing": False,
      "price": 400,
      "address": {
        "street-address": "1230 Main Street",
        "extended-address": "PO Box 1234",
        "locality": "Toronto",
        "region": "ON",
        "postal-code": "M7A 1T7",
        "country-name": "Canada"
      },
      "events": [
        {
          "start": "2023-11-25T10:30:00.000Z",
          "end": "2023-11-25T12:00:00.000Z"
        }
      ],
      "externalRegistrationUrl": "https://training-provider.com/reserve-seats/10012",
      "virtualClassUrl": "https://virtual-class-example.com/10001"
    }
    response = requests.patch(url, json=body, headers=headers)
    print(response.status_code)  # 204
    print(response.text)  # print(response.json())
    return response.text
def api_06_add_class_offering():
    print('06_add_class_offering')
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/ClassOffering"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIyYjU3MjNlNTEyN2I0Zjc1YTI5NDMxYzBkYTM0YTUyNSIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDA3NTE2MDMsImV4cCI6MTcwMDc5NDgwMywiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.Zxa_3Th3MtTuPjReHZkLen8ja-k2Pr5-KhZCQ2ri2CSzRXprVykKoJRjIdpST6PCKEzoOsgO-0EICChzrXpJ5ooxNjg9digwsjuGOlMzdJqHIss1328edhdvbxCTZ5gSCGaOSLD03aCxJrdV9vkr5yk5Lf04UQuPHwIxjfJ3gtNOtLJA5xUq5LdQWfks0RuEb2DNg6v8CIqvC7jqeljkhb2OoNb0gyaSKhsALHxd9oD1KykinK2J2rMQ9Z9pzIigRRTL4R0YqyrwZamaFzw3v-0D7buTDlVUsh62dx_27ebk0PcyR_wL_QUnbKOgWa8YlfE18lpxwgZHte22pV5KPQ",
        "key": "E933D1B3-3404-4EB5-A70F-B2128B3A2C6A",
        "Content-Type": "application/json"
    }
    body = {
      "offeringId": "wah-381",   # need to make a new ID any new call
      "trainingStandardKey": "WAH-10083",  # related to the Class ID inside the training programs schedules
      "deliveryMethod": "in-person",
      "courseName": "Working At Heights",
      "seatsRemaining": 10,
      "contactForPricing": False,
      "price": 300,
      "address": {
        "street-address": "169 fort york",
        "extended-address": "PO Box 1234",
        "locality": "Toronto",
        "region": "ON",
        "postal-code": "M5V 0C8",
        "country-name": "Canada"
      },
      "events": [
        {
          "start": "2023-11-24T10:30:00.000Z",
          "end": "2023-11-24T12:00:00.000Z"
        }
      ],
      "externalRegistrationUrl": "https://training-provider.com/reserve-seats/10012",
      "virtualClassUrl": "https://virtual-class-example.com/10001"
    }
    response = requests.post(url, json=body, headers=headers)
    print(response.status_code)  # 204
    print(response.text)  # print(response.json())
    return response.text
def api_07_add_learning_record():
    # Creating class using API, for same class View classroom > submitted records
    print('07_add_learning_record')
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/LearningRecord"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIyYjU3MjNlNTEyN2I0Zjc1YTI5NDMxYzBkYTM0YTUyNSIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDA3NTE2MDMsImV4cCI6MTcwMDc5NDgwMywiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.Zxa_3Th3MtTuPjReHZkLen8ja-k2Pr5-KhZCQ2ri2CSzRXprVykKoJRjIdpST6PCKEzoOsgO-0EICChzrXpJ5ooxNjg9digwsjuGOlMzdJqHIss1328edhdvbxCTZ5gSCGaOSLD03aCxJrdV9vkr5yk5Lf04UQuPHwIxjfJ3gtNOtLJA5xUq5LdQWfks0RuEb2DNg6v8CIqvC7jqeljkhb2OoNb0gyaSKhsALHxd9oD1KykinK2J2rMQ9Z9pzIigRRTL4R0YqyrwZamaFzw3v-0D7buTDlVUsh62dx_27ebk0PcyR_wL_QUnbKOgWa8YlfE18lpxwgZHte22pV5KPQ",
        "key": "E933D1B3-3404-4EB5-A70F-B2128B3A2C6A",
        "Content-Type": "application/json"
    }
    body = {
      "learningRecordId": "wah-381",
      "trainingStandardKey": "WAH-10083",
      "completionDate": "2023-12-12T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "wah-381",  # Need to match the ID of the class generated using the API's ClassOffering endpoint
      "instructorNames": "Jane Doe; Dave Weir",
      "evaluatorNames": "John Smith",
      "learner": {
        "uniqueId": "user-999",
        "firstname": "Peter",
        "lastname": "Johnson",
        "personalEmail": "perter.johnson@example.com",
        "birthYear": 1995,
        "address": {
          "street-address": "1230 Main Street",
          "extended-address": "PO Box 1234",
          "locality": "Toronto",
          "region": "ON",
          "postal-code": "M7A 1T7",
          "country-name": "Canada"
        },
        "mobilePhone": "6047771234",
        "homePhone": "7782225678"
      }
    }
    response = requests.post(url, json=body, headers=headers)
    print(response.status_code)  # 204
    print(response.text)  # print(response.json())
    return response.text



# latency
def api_15_response_time_delete_online_offering():
    print('Response_time')
    num_requests = 10  # Number of requests to send for testing
    max_response_time = 0
    total_response_time = 0
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/OnlineOffering/wah-131"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIyYjU3MjNlNTEyN2I0Zjc1YTI5NDMxYzBkYTM0YTUyNSIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDA3NTE2MDMsImV4cCI6MTcwMDc5NDgwMywiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.Zxa_3Th3MtTuPjReHZkLen8ja-k2Pr5-KhZCQ2ri2CSzRXprVykKoJRjIdpST6PCKEzoOsgO-0EICChzrXpJ5ooxNjg9digwsjuGOlMzdJqHIss1328edhdvbxCTZ5gSCGaOSLD03aCxJrdV9vkr5yk5Lf04UQuPHwIxjfJ3gtNOtLJA5xUq5LdQWfks0RuEb2DNg6v8CIqvC7jqeljkhb2OoNb0gyaSKhsALHxd9oD1KykinK2J2rMQ9Z9pzIigRRTL4R0YqyrwZamaFzw3v-0D7buTDlVUsh62dx_27ebk0PcyR_wL_QUnbKOgWa8YlfE18lpxwgZHte22pV5KPQ",
        "key": "E933D1B3-3404-4EB5-A70F-B2128B3A2C6A",
        "Content-Type": "application/json"
    }
    for i in range(num_requests):
        start_time = time.time()
        response = requests.delete(url, headers=headers)
        print(response.status_code)  # 204
        print(response.text)  # print(response.json())
        end_time = time.time()
        response_time = end_time - start_time
        total_response_time += response_time
        if response_time > max_response_time:
            max_response_time = response_time
    average_response_time = total_response_time / num_requests
    print('Number of requests ', num_requests)
    print('Average response time ', average_response_time)
    print('Maximum response time ', max_response_time)
def api_16_response_time_delete_class_offering():
    print('Response_time')
    num_requests = 10  # Number of requests to send for testing
    max_response_time = 0
    total_response_time = 0
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/ClassOffering/wah-131"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIyYjU3MjNlNTEyN2I0Zjc1YTI5NDMxYzBkYTM0YTUyNSIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDA3NTE2MDMsImV4cCI6MTcwMDc5NDgwMywiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.Zxa_3Th3MtTuPjReHZkLen8ja-k2Pr5-KhZCQ2ri2CSzRXprVykKoJRjIdpST6PCKEzoOsgO-0EICChzrXpJ5ooxNjg9digwsjuGOlMzdJqHIss1328edhdvbxCTZ5gSCGaOSLD03aCxJrdV9vkr5yk5Lf04UQuPHwIxjfJ3gtNOtLJA5xUq5LdQWfks0RuEb2DNg6v8CIqvC7jqeljkhb2OoNb0gyaSKhsALHxd9oD1KykinK2J2rMQ9Z9pzIigRRTL4R0YqyrwZamaFzw3v-0D7buTDlVUsh62dx_27ebk0PcyR_wL_QUnbKOgWa8YlfE18lpxwgZHte22pV5KPQ",
        "key": "E933D1B3-3404-4EB5-A70F-B2128B3A2C6A",
        "Content-Type": "application/json"
    }
    for i in range(num_requests):
        start_time = time.time()
        response = requests.delete(url, headers=headers)
        print(response.status_code)  # 204
        print(response.text)  # print(response.json())
        end_time = time.time()
        response_time = end_time - start_time
        total_response_time += response_time
        if response_time > max_response_time:
            max_response_time = response_time
    average_response_time = total_response_time / num_requests
    print('Number of requests ', num_requests)
    print('Average response time ', average_response_time)
    print('Maximum response time ', max_response_time)
def api_17_response_time_add_class_offering():
    print('Response_time')
    num_requests = 100  # Number of requests to send for testing
    max_response_time = 0
    total_response_time = 0
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/ClassOffering"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIyYjU3MjNlNTEyN2I0Zjc1YTI5NDMxYzBkYTM0YTUyNSIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDA3NTE2MDMsImV4cCI6MTcwMDc5NDgwMywiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.Zxa_3Th3MtTuPjReHZkLen8ja-k2Pr5-KhZCQ2ri2CSzRXprVykKoJRjIdpST6PCKEzoOsgO-0EICChzrXpJ5ooxNjg9digwsjuGOlMzdJqHIss1328edhdvbxCTZ5gSCGaOSLD03aCxJrdV9vkr5yk5Lf04UQuPHwIxjfJ3gtNOtLJA5xUq5LdQWfks0RuEb2DNg6v8CIqvC7jqeljkhb2OoNb0gyaSKhsALHxd9oD1KykinK2J2rMQ9Z9pzIigRRTL4R0YqyrwZamaFzw3v-0D7buTDlVUsh62dx_27ebk0PcyR_wL_QUnbKOgWa8YlfE18lpxwgZHte22pV5KPQ",
        "key": "E933D1B3-3404-4EB5-A70F-B2128B3A2C6A",
        "Content-Type": "application/json"
    }
    body = {
        "offeringId": "wah-383",  # need to make a new ID any new call
        "trainingStandardKey": "WAH-10083",  # related to the Class ID inside the training programs schedules
        "deliveryMethod": "in-person",
        "courseName": "Working At Heights",
        "seatsRemaining": 10,
        "contactForPricing": False,
        "price": 300,
        "address": {
            "street-address": "169 fort york",
            "extended-address": "PO Box 1234",
            "locality": "Toronto",
            "region": "ON",
            "postal-code": "M5V 0C8",
            "country-name": "Canada"
        },
        "events": [
            {
                "start": "2023-11-24T10:30:00.000Z",
                "end": "2023-11-24T12:00:00.000Z"
            }
        ],
        "externalRegistrationUrl": "https://training-provider.com/reserve-seats/10012",
        "virtualClassUrl": "https://virtual-class-example.com/10001"
    }
    for i in range(num_requests):
        start_time = time.time()
        response = requests.post(url, json=body, headers=headers)
        print(response.status_code)  # 204
        print(response.text)  # print(response.json())
        end_time = time.time()
        response_time = end_time - start_time
        total_response_time += response_time
        if response_time > max_response_time:
            max_response_time = response_time
    average_response_time = total_response_time / num_requests
    print('Number of requests ', num_requests)
    print('Average response time ', average_response_time)
    print('Maximum response time ', max_response_time)
def api_18_response_time_update_class_offering():
    print('Response_time')
    num_requests = 10  # Number of requests to send for testing
    max_response_time = 0
    total_response_time = 0
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/ClassOffering/wah-383"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIyYjU3MjNlNTEyN2I0Zjc1YTI5NDMxYzBkYTM0YTUyNSIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDA3NTE2MDMsImV4cCI6MTcwMDc5NDgwMywiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.Zxa_3Th3MtTuPjReHZkLen8ja-k2Pr5-KhZCQ2ri2CSzRXprVykKoJRjIdpST6PCKEzoOsgO-0EICChzrXpJ5ooxNjg9digwsjuGOlMzdJqHIss1328edhdvbxCTZ5gSCGaOSLD03aCxJrdV9vkr5yk5Lf04UQuPHwIxjfJ3gtNOtLJA5xUq5LdQWfks0RuEb2DNg6v8CIqvC7jqeljkhb2OoNb0gyaSKhsALHxd9oD1KykinK2J2rMQ9Z9pzIigRRTL4R0YqyrwZamaFzw3v-0D7buTDlVUsh62dx_27ebk0PcyR_wL_QUnbKOgWa8YlfE18lpxwgZHte22pV5KPQ",
        "key": "E933D1B3-3404-4EB5-A70F-B2128B3A2C6A",
        "Content-Type": "application/json"
    }
    body = {
      "courseName": "Working At Heights",
      "seatsRemaining": 15,
      "contactForPricing": False,
      "price": 400,
      "address": {
        "street-address": "1230 Main Street",
        "extended-address": "PO Box 1234",
        "locality": "Toronto",
        "region": "ON",
        "postal-code": "M7A 1T7",
        "country-name": "Canada"
      },
      "events": [
        {
          "start": "2023-11-25T10:30:00.000Z",
          "end": "2023-11-25T12:00:00.000Z"
        }
      ],
      "externalRegistrationUrl": "https://training-provider.com/reserve-seats/10012",
      "virtualClassUrl": "https://virtual-class-example.com/10001"
    }
    for i in range(num_requests):
        start_time = time.time()
        response = requests.patch(url, json=body, headers=headers)
        print(response.status_code)  # 204
        print(response.text)  # print(response.json())
        end_time = time.time()
        response_time = end_time - start_time
        total_response_time += response_time
        if response_time > max_response_time:
            max_response_time = response_time
    average_response_time = total_response_time / num_requests
    print('Number of requests ', num_requests)
    print('Average response time ', average_response_time)
    print('Maximum response time ', max_response_time)
def api_19_response_time_add_online_offering():
    print('Response_time')
    num_requests = 30  # Number of requests to send for testing
    max_response_time = 0
    total_response_time = 0
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/OnlineOffering"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIyYjU3MjNlNTEyN2I0Zjc1YTI5NDMxYzBkYTM0YTUyNSIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDA3NTE2MDMsImV4cCI6MTcwMDc5NDgwMywiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.Zxa_3Th3MtTuPjReHZkLen8ja-k2Pr5-KhZCQ2ri2CSzRXprVykKoJRjIdpST6PCKEzoOsgO-0EICChzrXpJ5ooxNjg9digwsjuGOlMzdJqHIss1328edhdvbxCTZ5gSCGaOSLD03aCxJrdV9vkr5yk5Lf04UQuPHwIxjfJ3gtNOtLJA5xUq5LdQWfks0RuEb2DNg6v8CIqvC7jqeljkhb2OoNb0gyaSKhsALHxd9oD1KykinK2J2rMQ9Z9pzIigRRTL4R0YqyrwZamaFzw3v-0D7buTDlVUsh62dx_27ebk0PcyR_wL_QUnbKOgWa8YlfE18lpxwgZHte22pV5KPQ",
        "key": "E933D1B3-3404-4EB5-A70F-B2128B3A2C6A",
        "Content-Type": "application/json"
    }
    body = {
      "offeringId": "wah-131",    # need to make a new ID any new call
      "trainingStandardKey": "JHSC-2014-1-10171",  # related to the Class ID inside the training programs schedules
      "courseName": "JHSC - Part One",
      "price": 111,
      "courseDuration": 4,
      "externalRegistrationUrl": "https://trainingproviderreservationsystem/register"
    }
    for i in range(num_requests):
        start_time = time.time()
        response = requests.post(url, json=body, headers=headers)
        print(response.status_code)  # 204
        print(response.text)  # print(response.json())
        end_time = time.time()
        response_time = end_time - start_time
        total_response_time += response_time
        if response_time > max_response_time:
            max_response_time = response_time
    average_response_time = total_response_time / num_requests
    print('Number of requests ', num_requests)
    print('Average response time ', average_response_time)
    print('Maximum response time ', max_response_time)
def api_20_response_time_update_online_offering():
    print('Response_time')
    num_requests = 30  # Number of requests to send for testing
    max_response_time = 0
    total_response_time = 0
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/OnlineOffering/wah-131"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIyYjU3MjNlNTEyN2I0Zjc1YTI5NDMxYzBkYTM0YTUyNSIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDA3NTE2MDMsImV4cCI6MTcwMDc5NDgwMywiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.Zxa_3Th3MtTuPjReHZkLen8ja-k2Pr5-KhZCQ2ri2CSzRXprVykKoJRjIdpST6PCKEzoOsgO-0EICChzrXpJ5ooxNjg9digwsjuGOlMzdJqHIss1328edhdvbxCTZ5gSCGaOSLD03aCxJrdV9vkr5yk5Lf04UQuPHwIxjfJ3gtNOtLJA5xUq5LdQWfks0RuEb2DNg6v8CIqvC7jqeljkhb2OoNb0gyaSKhsALHxd9oD1KykinK2J2rMQ9Z9pzIigRRTL4R0YqyrwZamaFzw3v-0D7buTDlVUsh62dx_27ebk0PcyR_wL_QUnbKOgWa8YlfE18lpxwgZHte22pV5KPQ",
        "key": "E933D1B3-3404-4EB5-A70F-B2128B3A2C6A",
        "Content-Type": "application/json"
    }
    body = {
      "courseName": "JHSC - Part One",
      "price": 222,
      "courseDuration": 3,
      "externalRegistrationUrl": "https://trainingproviderreservationsystem/register"
    }
    for i in range(num_requests):
        start_time = time.time()
        response = requests.patch(url, json=body, headers=headers)
        print(response.status_code)  # 204
        print(response.text)  # print(response.json())
        end_time = time.time()
        response_time = end_time - start_time
        total_response_time += response_time
        if response_time > max_response_time:
            max_response_time = response_time
    average_response_time = total_response_time / num_requests
    print('Number of requests ', num_requests)
    print('Average response time ', average_response_time)
    print('Maximum response time ', max_response_time)
def api_21_response_time_add_learning_record():
    print('Response_time')
    num_requests = 30  # Number of requests to send for testing
    max_response_time = 0
    total_response_time = 0
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/LearningRecord"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIyYjU3MjNlNTEyN2I0Zjc1YTI5NDMxYzBkYTM0YTUyNSIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDA3NTE2MDMsImV4cCI6MTcwMDc5NDgwMywiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.Zxa_3Th3MtTuPjReHZkLen8ja-k2Pr5-KhZCQ2ri2CSzRXprVykKoJRjIdpST6PCKEzoOsgO-0EICChzrXpJ5ooxNjg9digwsjuGOlMzdJqHIss1328edhdvbxCTZ5gSCGaOSLD03aCxJrdV9vkr5yk5Lf04UQuPHwIxjfJ3gtNOtLJA5xUq5LdQWfks0RuEb2DNg6v8CIqvC7jqeljkhb2OoNb0gyaSKhsALHxd9oD1KykinK2J2rMQ9Z9pzIigRRTL4R0YqyrwZamaFzw3v-0D7buTDlVUsh62dx_27ebk0PcyR_wL_QUnbKOgWa8YlfE18lpxwgZHte22pV5KPQ",
        "key": "E933D1B3-3404-4EB5-A70F-B2128B3A2C6A",
        "Content-Type": "application/json"
    }
    body = {
      "learningRecordId": "wah-350",
      "trainingStandardKey": "WAH-10083",
      "completionDate": "2023-12-12T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "wah-381",  # Need to match the ID of the class generated using the API's ClassOffering endpoint
      "instructorNames": "Jane Doe; Dave Weir",
      "evaluatorNames": "John Smith",
      "learner": {
        "uniqueId": "user-999",
        "firstname": "Peter",
        "lastname": "Johnson",
        "personalEmail": "perter.johnson@example.com",
        "birthYear": 1995,
        "address": {
          "street-address": "1230 Main Street",
          "extended-address": "PO Box 1234",
          "locality": "Toronto",
          "region": "ON",
          "postal-code": "M7A 1T7",
          "country-name": "Canada"
        },
        "mobilePhone": "6047771234",
        "homePhone": "7782225678"
      }
    }
    for i in range(num_requests):
        start_time = time.time()
        response = requests.post(url, json=body, headers=headers)
        print(response.status_code)  # 204
        print(response.text)  # print(response.json())
        end_time = time.time()
        response_time = end_time - start_time
        total_response_time += response_time
        if response_time > max_response_time:
            max_response_time = response_time
    average_response_time = total_response_time / num_requests
    print('Number of requests ', num_requests)
    print('Average response time ', average_response_time)
    print('Maximum response time ', max_response_time)







