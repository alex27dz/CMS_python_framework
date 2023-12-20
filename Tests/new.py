import base64
from urllib.parse import urlencode
import requests
import api
import pytest
import time


# APIs
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
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIzZDBhNTAzOGM5ODY0YzAzYjI2OThkMzU1ODZlNWYwMiIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDIzOTg3ODIsImV4cCI6MTcwMjQ0MTk4MiwiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.JR1NdqurojMDJo4OtUYdpeAU56JyNnQ3EF7heTnNbrRd3lOoyAQ49bq4S5_47VAB_DgQ9YyD-5GeOpIbXaIkjlCfPXdRPV2jFr2lTB9Xesv6mxaLNKk1o04mRsFguSOaiTXhubqmc9E9dZAFSBRf6cfHHTS3Z9W9pC2cmF3-Cdu-tL96KdgE6C2lmNVeeztooGhMgkeC04k17LoOztFO8yzI76vOiGCE3vvwNT1cMT4xrVeP39rcOx4VrqxLj31tznZpFL8a9p9Z1xo1GRkv41muEscXrrtR4SD46PVcCP8TGzCfw0KILKUqHmq4HkNxRfyDN__OESMDU5t1TrYSgQ",
        "key": "E933D1B3-3404-4EB5-A70F-B2128B3A2C6A",
        "Content-Type": "application/json"
    }
    body = {  #  JHSC-2014-1-10149   JHSC-2014-1-10171
      "offeringId": "wah-133",    # need to make a new ID any new call
      "trainingStandardKey": "JHSC-2014-1-10171",  # related to the Class ID inside the training programs schedules
      "courseName": "JHSC - Part One",
      "price": 12000,
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
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI4ODQ2YjYzNjVkYzE0NzRmOWYyYjBjMmJhMjJlNGJkNiIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDA4Mzc5NTEsImV4cCI6MTcwMDg4MTE1MSwiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.VNDA47KmG6q6QuAgpxfQ3iZ8Gwq-HdHbfETB0y_kSv3S5giHRAzks0GvFd9DvhOd6Hl3Hxy7-N4yg-OJRwWbXaTOxydxywWeDFC5Rqim1dvZ737CCO3RjIOb94W4Luxt7J8dH8bPRwk-2LlAryevKs4OASmn3NY8jBFSi6rYKO5029S5OvBm8KNVQYoQdmgQMBveLEtJFtQAUag6HK5N9r17eYH7a39_35V5zrf-DtqnuQMb1NlZ73THzxhINYPIsF_yBrUyNPD7E4ZNRi3iOyXyfIr5ng5y86yju5ZWvskNH62jvRQ_jzVTaWpq7-37tpbzBGnxfEALfjI-tojLcg",
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
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIzZDBhNTAzOGM5ODY0YzAzYjI2OThkMzU1ODZlNWYwMiIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDIzOTg3ODIsImV4cCI6MTcwMjQ0MTk4MiwiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.JR1NdqurojMDJo4OtUYdpeAU56JyNnQ3EF7heTnNbrRd3lOoyAQ49bq4S5_47VAB_DgQ9YyD-5GeOpIbXaIkjlCfPXdRPV2jFr2lTB9Xesv6mxaLNKk1o04mRsFguSOaiTXhubqmc9E9dZAFSBRf6cfHHTS3Z9W9pC2cmF3-Cdu-tL96KdgE6C2lmNVeeztooGhMgkeC04k17LoOztFO8yzI76vOiGCE3vvwNT1cMT4xrVeP39rcOx4VrqxLj31tznZpFL8a9p9Z1xo1GRkv41muEscXrrtR4SD46PVcCP8TGzCfw0KILKUqHmq4HkNxRfyDN__OESMDU5t1TrYSgQ",
        "key": "E933D1B3-3404-4EB5-A70F-B2128B3A2C6A",
        "Content-Type": "application/json"
    }
    # WAH-10083
    # JHSC-2014-1-10171
    body = {
      "offeringId": "wah-383",   # need to make a new ID any new call
      "trainingStandardKey": "WAH-10083",  # related to the Class ID inside the training programs schedules
      "deliveryMethod": "in-person",
      "courseName": "Working At Heights",
      "seatsRemaining": 10,
      "contactForPricing": False,
      "price": 900,
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
          "start": "2023-12-13T10:30:00.000Z",
          "end": "2023-12-13T12:00:00.000Z"
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
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIzZDBhNTAzOGM5ODY0YzAzYjI2OThkMzU1ODZlNWYwMiIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDIzOTg3ODIsImV4cCI6MTcwMjQ0MTk4MiwiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.JR1NdqurojMDJo4OtUYdpeAU56JyNnQ3EF7heTnNbrRd3lOoyAQ49bq4S5_47VAB_DgQ9YyD-5GeOpIbXaIkjlCfPXdRPV2jFr2lTB9Xesv6mxaLNKk1o04mRsFguSOaiTXhubqmc9E9dZAFSBRf6cfHHTS3Z9W9pC2cmF3-Cdu-tL96KdgE6C2lmNVeeztooGhMgkeC04k17LoOztFO8yzI76vOiGCE3vvwNT1cMT4xrVeP39rcOx4VrqxLj31tznZpFL8a9p9Z1xo1GRkv41muEscXrrtR4SD46PVcCP8TGzCfw0KILKUqHmq4HkNxRfyDN__OESMDU5t1TrYSgQ",
        "key": "E933D1B3-3404-4EB5-A70F-B2128B3A2C6A",
        "Content-Type": "application/json"
    }
    body = {
      "learningRecordId": "wah-383",
      "trainingStandardKey": "WAH-10083",
      "completionDate": "2023-12-14T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "wah-383",  # Need to match the ID of the class generated using the API's ClassOffering endpoint
      "instructorNames": "alex doe; alexander",
      "evaluatorNames": "will Smith",
      "learner": {
        "uniqueId": "user-112",
        "firstname": "Alexander",
        "lastname": "Pasqua",
        "personalEmail": "Alexander@email.com",  # need to be changed for new record creations within the same class
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


body1 = {
      "learningRecordId": "wah-381",
      "trainingStandardKey": "WAH-10083",
      "completionDate": "2023-12-12T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "wah-381",  # Need to match the ID of the class generated using the API's ClassOffering endpoint
      "instructorNames": "Jane Doe; Dave Weir",
      "evaluatorNames": "John Smith",
      "learner": {
        "uniqueId": "user-112",
        "firstname": "adam",
        "lastname": "Adam",
        "personalEmail": "adam1.johnson@example.com",  # need to be changed for new record creations within the same class
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
body2 = {
      "learningRecordId": "wah-381",
      "trainingStandardKey": "WAH-10083",
      "completionDate": "2023-12-12T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "wah-381",  # Need to match the ID of the class generated using the API's ClassOffering endpoint
      "instructorNames": "Jane Doe; Dave Weir",
      "evaluatorNames": "John Smith",
      "learner": {
        "uniqueId": "user-112",
        "firstname": "adam",
        "lastname": "Adam",
        "personalEmail": "adam2.johnson@example.com",  # need to be changed for new record creations within the same class
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
body3 = {
      "learningRecordId": "wah-381",
      "trainingStandardKey": "WAH-10083",
      "completionDate": "2023-12-12T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "wah-381",  # Need to match the ID of the class generated using the API's ClassOffering endpoint
      "instructorNames": "Jane Doe; Dave Weir",
      "evaluatorNames": "John Smith",
      "learner": {
        "uniqueId": "user-112",
        "firstname": "adam",
        "lastname": "Adam",
        "personalEmail": "adam3.johnson@example.com",  # need to be changed for new record creations within the same class
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
body4 = {
      "learningRecordId": "wah-381",
      "trainingStandardKey": "WAH-10083",
      "completionDate": "2023-12-12T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "wah-381",  # Need to match the ID of the class generated using the API's ClassOffering endpoint
      "instructorNames": "Jane Doe; Dave Weir",
      "evaluatorNames": "John Smith",
      "learner": {
        "uniqueId": "user-112",
        "firstname": "adam",
        "lastname": "Adam",
        "personalEmail": "adam4.johnson@example.com",  # need to be changed for new record creations within the same class
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
body5 = {
      "learningRecordId": "wah-381",
      "trainingStandardKey": "WAH-10083",
      "completionDate": "2023-12-12T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "wah-381",  # Need to match the ID of the class generated using the API's ClassOffering endpoint
      "instructorNames": "Jane Doe; Dave Weir",
      "evaluatorNames": "John Smith",
      "learner": {
        "uniqueId": "user-112",
        "firstname": "adam",
        "lastname": "Adam",
        "personalEmail": "adam5.johnson@example.com",  # need to be changed for new record creations within the same class
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
body6 = {
      "learningRecordId": "wah-381",
      "trainingStandardKey": "WAH-10083",
      "completionDate": "2023-12-12T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "wah-381",  # Need to match the ID of the class generated using the API's ClassOffering endpoint
      "instructorNames": "Jane Doe; Dave Weir",
      "evaluatorNames": "John Smith",
      "learner": {
        "uniqueId": "user-112",
        "firstname": "adam",
        "lastname": "Adam",
        "personalEmail": "adam6.johnson@example.com",  # need to be changed for new record creations within the same class
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
body7 = {
      "learningRecordId": "wah-381",
      "trainingStandardKey": "WAH-10083",
      "completionDate": "2023-12-12T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "wah-381",  # Need to match the ID of the class generated using the API's ClassOffering endpoint
      "instructorNames": "Jane Doe; Dave Weir",
      "evaluatorNames": "John Smith",
      "learner": {
        "uniqueId": "user-112",
        "firstname": "adam",
        "lastname": "Adam",
        "personalEmail": "adam7.johnson@example.com",  # need to be changed for new record creations within the same class
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
body8 = {
      "learningRecordId": "wah-381",
      "trainingStandardKey": "WAH-10083",
      "completionDate": "2023-12-12T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "wah-381",  # Need to match the ID of the class generated using the API's ClassOffering endpoint
      "instructorNames": "Jane Doe; Dave Weir",
      "evaluatorNames": "John Smith",
      "learner": {
        "uniqueId": "user-112",
        "firstname": "adam",
        "lastname": "Adam",
        "personalEmail": "adam8.johnson@example.com",  # need to be changed for new record creations within the same class
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
body9 = {
      "learningRecordId": "wah-381",
      "trainingStandardKey": "WAH-10083",
      "completionDate": "2023-12-12T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "wah-381",  # Need to match the ID of the class generated using the API's ClassOffering endpoint
      "instructorNames": "Jane Doe; Dave Weir",
      "evaluatorNames": "John Smith",
      "learner": {
        "uniqueId": "user-112",
        "firstname": "adam",
        "lastname": "Adam",
        "personalEmail": "adam9.johnson@example.com",  # need to be changed for new record creations within the same class
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
body10 = {
      "learningRecordId": "wah-381",
      "trainingStandardKey": "WAH-10083",
      "completionDate": "2023-12-12T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "wah-381",  # Need to match the ID of the class generated using the API's ClassOffering endpoint
      "instructorNames": "Jane Doe; Dave Weir",
      "evaluatorNames": "John Smith",
      "learner": {
        "uniqueId": "user-112",
        "firstname": "adam",
        "lastname": "Adam",
        "personalEmail": "adam10.johnson@example.com",  # need to be changed for new record creations within the same class
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
listofbodyapi = [body1, body2, body3, body4, body5, body6, body7, body8, body9, body10]


def api_22_response_time_add_10_learning_records():
    print('Response_time')
    num_requests = 10  # Number of requests to send for testing
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
        response = requests.post(url, json=listofbodyapi[i], headers=headers)
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







