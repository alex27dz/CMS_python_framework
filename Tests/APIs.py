import base64
from urllib.parse import urlencode
import requests
import api
import pytest
import time
'''
https://stage.apps.labour.gov.on.ca/api-facade-uat/ClassOffering
https://stage.apps.labour.gov.on.ca/api-facade-uat/OnlineOffering
https://stage.apps.labour.gov.on.ca/api-facade-uat/LearningRecord
'''


# APIs
def sso_00_token():
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


# Online Class
def api_01_delete_online_offering():
    print('api_01_delete_online_offering')
    url = "https://stage.apps.labour.gov.on.ca/api-facade-uat/OnlineOffering/wah-150"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI0ZGM0MjI0YjAyZDQ0YTNmYWQ5ZDg0NDQ1N2I3YzVhMCIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDYwNDU5ODcsImV4cCI6MTcwNjA4OTE4NywiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.OhJLolbDKZjt_a-wMAWLGJYxjDOGwX7xFDe3pp6T3dFD-d4r8zmcu2jowKAZRpECj8Z11mlussNNgP4k6J-gNdSE_s2Ukyj6M1r45L7h6-uRtD82b4o6YjJ-MTFsVyd7i1X4CwjwqRZTKQXgh_2fDARxWcta0PcKe3a0WCLyLRNurlWf4GEbX2w6nh_6GQ0mkEnVHgTW3VzyAp1Y0B202WYY2Ks0WIiybZmz1YUwY4cuYWw3bqLdkziDrRPVUmXv35-jc8C4mSsdiubvUpseaGyNoJkyG2vHxGld4kBU9qPzNDncbQmO3yjf3BymVy-I5yISgekrEL-fLgegvjf4dA",
        "key": "96593687-6755-45DE-9E71-2FA3BA8CB3D0",
        "Content-Type": "application/json; charset=utf-8"
    }
    response = requests.delete(url, headers=headers)
    print(response.status_code)  # 204
    print(response.text)  # print(response.json())
    return response.text
api_01_delete_online_offering()
def api_02_update_online_offering():
    print('02_update_online_offerings')
    url = "https://stage.apps.labour.gov.on.ca/api-facade-uat/OnlineOffering/wah-150"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI0ZGM0MjI0YjAyZDQ0YTNmYWQ5ZDg0NDQ1N2I3YzVhMCIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDYwNDU5ODcsImV4cCI6MTcwNjA4OTE4NywiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.OhJLolbDKZjt_a-wMAWLGJYxjDOGwX7xFDe3pp6T3dFD-d4r8zmcu2jowKAZRpECj8Z11mlussNNgP4k6J-gNdSE_s2Ukyj6M1r45L7h6-uRtD82b4o6YjJ-MTFsVyd7i1X4CwjwqRZTKQXgh_2fDARxWcta0PcKe3a0WCLyLRNurlWf4GEbX2w6nh_6GQ0mkEnVHgTW3VzyAp1Y0B202WYY2Ks0WIiybZmz1YUwY4cuYWw3bqLdkziDrRPVUmXv35-jc8C4mSsdiubvUpseaGyNoJkyG2vHxGld4kBU9qPzNDncbQmO3yjf3BymVy-I5yISgekrEL-fLgegvjf4dA",
        "key": "96593687-6755-45DE-9E71-2FA3BA8CB3D0",
        "Content-Type": "application/json"
    }
    body = {
      "courseName": "JHSC - Part One",  # not appears on UI
      "price": 300000,
      "courseDuration": 2,  # not appears on UI
      "externalRegistrationUrl": "https://trainingproviderreservationsystem/register"  # not appears on UI
    }
    response = requests.patch(url, json=body, headers=headers)
    print(response.status_code)  # 204
    print(response.text)  # print(response.json())
    return response.text
def api_03_add_online_offering():
    print('03_add_online_offering')
    url = "https://stage.apps.labour.gov.on.ca/api-facade-uat/OnlineOffering"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI0ZGM0MjI0YjAyZDQ0YTNmYWQ5ZDg0NDQ1N2I3YzVhMCIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDYwNDU5ODcsImV4cCI6MTcwNjA4OTE4NywiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.OhJLolbDKZjt_a-wMAWLGJYxjDOGwX7xFDe3pp6T3dFD-d4r8zmcu2jowKAZRpECj8Z11mlussNNgP4k6J-gNdSE_s2Ukyj6M1r45L7h6-uRtD82b4o6YjJ-MTFsVyd7i1X4CwjwqRZTKQXgh_2fDARxWcta0PcKe3a0WCLyLRNurlWf4GEbX2w6nh_6GQ0mkEnVHgTW3VzyAp1Y0B202WYY2Ks0WIiybZmz1YUwY4cuYWw3bqLdkziDrRPVUmXv35-jc8C4mSsdiubvUpseaGyNoJkyG2vHxGld4kBU9qPzNDncbQmO3yjf3BymVy-I5yISgekrEL-fLgegvjf4dA",
        "key": "96593687-6755-45DE-9E71-2FA3BA8CB3D0",
        "Content-Type": "application/json"
    }
    body = {  #  JHSC-2014-1-10149   JHSC-2014-1-10171
      "offeringId": "wah-150",    # need to make a new ID any new call
      "trainingStandardKey": "JHSC-2014-1-10101",  # related to the Class ID inside the training programs schedules
      "courseName": "JHSC - Part One",
      "price": 260000,
      "courseDuration": 4,
      "externalRegistrationUrl": "https://trainingproviderreservationsystem/register"
    }
    response = requests.post(url, json=body, headers=headers)
    print(response.status_code)  # 204
    print(response.text)  # print(response.json())
    return response.text

# Regular Class
def api_04_delete_class_offering():
    print('04_delete_class_offerings')
    url = "https://stage.apps.labour.gov.on.ca/api-facade-uat/ClassOffering/wah-385"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI0ZGM0MjI0YjAyZDQ0YTNmYWQ5ZDg0NDQ1N2I3YzVhMCIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDYwNDU5ODcsImV4cCI6MTcwNjA4OTE4NywiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.OhJLolbDKZjt_a-wMAWLGJYxjDOGwX7xFDe3pp6T3dFD-d4r8zmcu2jowKAZRpECj8Z11mlussNNgP4k6J-gNdSE_s2Ukyj6M1r45L7h6-uRtD82b4o6YjJ-MTFsVyd7i1X4CwjwqRZTKQXgh_2fDARxWcta0PcKe3a0WCLyLRNurlWf4GEbX2w6nh_6GQ0mkEnVHgTW3VzyAp1Y0B202WYY2Ks0WIiybZmz1YUwY4cuYWw3bqLdkziDrRPVUmXv35-jc8C4mSsdiubvUpseaGyNoJkyG2vHxGld4kBU9qPzNDncbQmO3yjf3BymVy-I5yISgekrEL-fLgegvjf4dA",
        "key": "96593687-6755-45DE-9E71-2FA3BA8CB3D0",
        # 96593687-6755-45DE-9E71-2FA3BA8CB3D0  # E933D1B3-3404-4EB5-A70F-B2128B3A2C6A
        "Content-Type": "application/json; charset=utf-8"
    }

    response = requests.delete(url, headers=headers)
    print(response.status_code)  # 204
    print(response.text)  # print(response.json())
    return response.text
def api_05_update_class_offering():
    print('05_update_class_offerings')
    url = "https://stage.apps.labour.gov.on.ca/api-facade-uat/ClassOffering/wah-385"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI0ZGM0MjI0YjAyZDQ0YTNmYWQ5ZDg0NDQ1N2I3YzVhMCIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDYwNDU5ODcsImV4cCI6MTcwNjA4OTE4NywiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.OhJLolbDKZjt_a-wMAWLGJYxjDOGwX7xFDe3pp6T3dFD-d4r8zmcu2jowKAZRpECj8Z11mlussNNgP4k6J-gNdSE_s2Ukyj6M1r45L7h6-uRtD82b4o6YjJ-MTFsVyd7i1X4CwjwqRZTKQXgh_2fDARxWcta0PcKe3a0WCLyLRNurlWf4GEbX2w6nh_6GQ0mkEnVHgTW3VzyAp1Y0B202WYY2Ks0WIiybZmz1YUwY4cuYWw3bqLdkziDrRPVUmXv35-jc8C4mSsdiubvUpseaGyNoJkyG2vHxGld4kBU9qPzNDncbQmO3yjf3BymVy-I5yISgekrEL-fLgegvjf4dA",
        "key": "96593687-6755-45DE-9E71-2FA3BA8CB3D0",
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
          "start": "2023-01-24T10:30:00.000Z",
          "end": "2023-01-24T12:00:00.000Z"
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
    url = "https://stage.apps.labour.gov.on.ca/api-facade-uat/ClassOffering"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI0ZGM0MjI0YjAyZDQ0YTNmYWQ5ZDg0NDQ1N2I3YzVhMCIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDYwNDU5ODcsImV4cCI6MTcwNjA4OTE4NywiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.OhJLolbDKZjt_a-wMAWLGJYxjDOGwX7xFDe3pp6T3dFD-d4r8zmcu2jowKAZRpECj8Z11mlussNNgP4k6J-gNdSE_s2Ukyj6M1r45L7h6-uRtD82b4o6YjJ-MTFsVyd7i1X4CwjwqRZTKQXgh_2fDARxWcta0PcKe3a0WCLyLRNurlWf4GEbX2w6nh_6GQ0mkEnVHgTW3VzyAp1Y0B202WYY2Ks0WIiybZmz1YUwY4cuYWw3bqLdkziDrRPVUmXv35-jc8C4mSsdiubvUpseaGyNoJkyG2vHxGld4kBU9qPzNDncbQmO3yjf3BymVy-I5yISgekrEL-fLgegvjf4dA",
        "key": "96593687-6755-45DE-9E71-2FA3BA8CB3D0",
        "Content-Type": "application/json"
    }
    # WAH-10083
    # JHSC-2014-1-10171
    body = {
      "offeringId": "wah-385",   # need to make a new ID any new call
      "trainingStandardKey": "JHSC-2014-2-10096",  # related to the Class ID inside the training programs schedules
      "deliveryMethod": "in-person",
      "courseName": "Working At Heights",
      "seatsRemaining": 10,
      "contactForPricing": False,
      "price": 20000,
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
          "start": "2024-01-24T10:30:00.000Z",
          "end": "2024-01-24T12:00:00.000Z"
        }
      ],
      "externalRegistrationUrl": "https://training-provider.com/reserve-seats/10012",
      "virtualClassUrl": "https://virtual-class-example.com/10001"
    }
    response = requests.post(url, json=body, headers=headers)
    print(response.status_code)  # 204
    print(response.text)  # print(response.json())
    return response.text


# Online + Regular Class
def api_07_add_learning_record():
    # Creating class using API, for same class View classroom > submitted records
    print('07_add_learning_record')
    url = "https://stage.apps.labour.gov.on.ca/api-facade-uat/LearningRecord"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYWRmc29uZWtleS1hdXRoLnVhYS5zeXMudWF0LmNmLmF6LmNpaHMuZ292Lm9uLmNhL3Rva2VuX2tleXMiLCJraWQiOiJrZXktMSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI0ZGM0MjI0YjAyZDQ0YTNmYWQ5ZDg0NDQ1N2I3YzVhMCIsInN1YiI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF1dGhvcml0aWVzIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sInNjb3BlIjpbInVhYS5yZXNvdXJjZSIsImNtcy1mYWNhZGUuYXV0aG9yaXplIl0sImNsaWVudF9pZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImNpZCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImF6cCI6IjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiYTBiMWZiNzkiLCJpYXQiOjE3MDYwNDU5ODcsImV4cCI6MTcwNjA4OTE4NywiaXNzIjoiaHR0cHM6Ly9hZGZzb25la2V5LWF1dGgudWFhLnN5cy51YXQuY2YuYXouY2locy5nb3Yub24uY2Evb2F1dGgvdG9rZW4iLCJ6aWQiOiJmODAzNWM5OS0xY2VjLTQyM2MtYTYyYi1lNTM1ZGRhZmY2ZjEiLCJhdWQiOlsiY21zLWZhY2FkZSIsInVhYSIsIjUzYzQwODQ0LTk5Y2EtNDE0Ny04NzE5LTc4ZWZhNTM2YmNmNCJdfQ.OhJLolbDKZjt_a-wMAWLGJYxjDOGwX7xFDe3pp6T3dFD-d4r8zmcu2jowKAZRpECj8Z11mlussNNgP4k6J-gNdSE_s2Ukyj6M1r45L7h6-uRtD82b4o6YjJ-MTFsVyd7i1X4CwjwqRZTKQXgh_2fDARxWcta0PcKe3a0WCLyLRNurlWf4GEbX2w6nh_6GQ0mkEnVHgTW3VzyAp1Y0B202WYY2Ks0WIiybZmz1YUwY4cuYWw3bqLdkziDrRPVUmXv35-jc8C4mSsdiubvUpseaGyNoJkyG2vHxGld4kBU9qPzNDncbQmO3yjf3BymVy-I5yISgekrEL-fLgegvjf4dA",
        "key": "96593687-6755-45DE-9E71-2FA3BA8CB3D0",
        "Content-Type": "application/json"
    }
    body = {
      "learningRecordId": "wah-150",
      "trainingStandardKey": "JHSC-2014-1-10101",
      "completionDate": "2024-01-22T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "wah-150",  # Need to match the ID of the class generated using the API's ClassOffering endpoint
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




