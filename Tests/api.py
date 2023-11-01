import requests
import api
import pytest

'''
API requests are the mechanisms by which one software application sends a request to another application's API to perform certain actions or retrieve specific information
Components of an API Request:
* HTTP Method (Request Verb): The HTTP method specifies the type of action you want to perform on the resource. Common methods include:
    * GET: Retrieve data from the server.
    * POST: ADD/Send data to the server to create a new resource.
    * PUT: Update an existing resource on the server.
    * DELETE: Delete a resource on the server.
    * PATCH: Update method is used to make partial updates to a resource on the server
* URL (Uniform Resource Locator): The URL identifies the specific endpoint (resource) on the server that the request is targeting.
* Headers: Headers provide additional information about the request, such as authentication tokens, content type, and more.
* Request Body (Optional): For methods like POST and PUT, the request body contains the data you're sending to the server.
API Response:
After sending an API request, the server processes the request and sends back an API response.
The response typically includes:
    * Status Code: A three-digit code indicating the outcome of the request (e.g., 200 for success, 404 for not found, 500 for internal server error).
    * Headers: Additional metadata about the response.
    * Response Body: The actual data sent by the server in response to the request. This can be in various formats like JSON, XML, HTML, etc.
Authentication:
Many APIs require authentication to ensure only authorized users can access their resources.
This is often done using tokens (API keys, access tokens, etc.) that are included in the request headers.

1
https://netsdc.visualstudio.com/SDC/_workitems/edit/98391
2
https://netsdc.visualstudio.com/SDC/_workitems/edit/98387
3
https://netsdc.visualstudio.com/SDC/_workitems/edit/98383
4
https://netsdc.visualstudio.com/SDC/_workitems/edit/98377
5
https://netsdc.visualstudio.com/SDC/_workitems/edit/98372
6
https://netsdc.visualstudio.com/SDC/_workitems/edit/98194/
7
https://netsdc.visualstudio.com/SDC/_workitems/edit/98393

* Online offering = Class inside 'my training schedules' list 'Elearning'	https://intra.stage.apps.labour.gov.on.ca/public-portal-qa/training-provider/training-schedules
* Class offerings	https://intra.stage.apps.labour.gov.on.ca/public-portal-qa/training-provider/training-schedules
* Learning records	https://intra.stage.apps.labour.gov.on.ca/public-portal-qa/training-provider/training-schedules (Record created inside an API created class)
* Course marketplace	https://intra.stage.apps.labour.gov.on.ca/public-portal-qa/marketplace/course-search 

'''

# DELETE - online offering - offeringId, Result - Course, ElectronicAddressOwnership, & ElectronicAddress - deleted
def api_01_delete_online_offering_98391():
    print('01_delete_online_offerings')
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/ClassOffering"  # YOUR OFFERING ID HERE
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwia2V5IjoiRTkzM0QxQjMtMzQwNC00RUI1LUE3MEYtQjIxMjhCM0EyQzZBIn0.f3daVM-MZy8idhskfmafSdcZw6mwIiEzBze7UCZ2V6A",
        "Content-Type": "application/json; charset=utf-8"
    }
    body = {
      "offeringId": "ae555337-ca58-46a1-9471-a323a3dbdc85"
    }
    response = requests.delete(url, json=body, headers=headers)
    print(response.status_code)  # 204
    print(response.text)  # print(response.json())
    return response.text
# UPDATE - online offering
def api_02_update_online_offering_98387():
    print('02_update_online_offerings')
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/ClassOffering"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwia2V5IjoiRTkzM0QxQjMtMzQwNC00RUI1LUE3MEYtQjIxMjhCM0EyQzZBIn0.f3daVM-MZy8idhskfmafSdcZw6mwIiEzBze7UCZ2V6A",
        "Content-Type": "application/json"
    }
    body = {
      "courseName": "Working At Heights E-Learning",
      "price": 100,
      "courseDuration": 2.5,
      "externalRegistrationUrl": "https://trainingproviderreservationsystem/register"
    }
    response = requests.patch(url, json=body, headers=headers)
    print(response.status_code)  # 204
    print(response.text)  # print(response.json())
    return response.text
# ADD - online offering
def api_03_add_online_offering_98383():
    print('03_add_online_offerings')
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/OnlineOffering"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwia2V5IjoiRTkzM0QxQjMtMzQwNC00RUI1LUE3MEYtQjIxMjhCM0EyQzZBIn0.f3daVM-MZy8idhskfmafSdcZw6mwIiEzBze7UCZ2V6A",
        "Content-Type": "application/json"
    }
    body = {
      "offeringId": "wah-111",
      "trainingStandardKey": "WAH-E-B-O",
      "courseName": "Working At Heights",
      "price": 100,
      "courseDuration": 2.5,
      "externalRegistrationUrl": "https://trainingproviderreservationsystem/register"
    }
    response = requests.post(url, json=body, headers=headers)
    print(response.status_code)  # 204
    print(response.text)  # print(response.json())
    return response.text
# DELETE - class offering
def api_04_delete_class_offering_98377():
    print('04_delete_class_offerings')
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/OnlineOffering"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwia2V5IjoiRTkzM0QxQjMtMzQwNC00RUI1LUE3MEYtQjIxMjhCM0EyQzZBIn0.f3daVM-MZy8idhskfmafSdcZw6mwIiEzBze7UCZ2V6A",
        "Content-Type": "application/json; charset=utf-8"
    }
    body = {
      "offeringId": "external-class-id"
    }
    response = requests.delete(url, json=body, headers=headers)
    print(response.status_code)  # 204
    print(response.text)  # print(response.json())
    return response.text
# UPDATE - class offering
def api_05_update_class_offering_98372():
    print('05_update_class_offerings')
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/OnlineOffering"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwia2V5IjoiRTkzM0QxQjMtMzQwNC00RUI1LUE3MEYtQjIxMjhCM0EyQzZBIn0.f3daVM-MZy8idhskfmafSdcZw6mwIiEzBze7UCZ2V6A",
        "Content-Type": "application/json"
    }
    body = {
      "courseName": "Working At Heights",
      "seatsRemaining": 5,
      "contactForPricing": True,
      "price": 100,
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
          "start": "2018-11-21T10:30:00.000Z",
          "end": "2018-11-21T12:00:00.000Z"
        }
      ],
      "externalRegistrationUrl": "https://training-provider.com/reserve-seats/10012",
      "virtualClassUrl": "https://virtual-class-example.com/10001"
    }
    response = requests.patch(url, json=body, headers=headers)
    print(response.status_code)  # 204
    print(response.text)  # print(response.json())
    return response.text
# ADD - class offering
def api_06_add_class_offering_98194():
    print('06_add_class_offering')
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/ClassOffering"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwia2V5IjoiRTkzM0QxQjMtMzQwNC00RUI1LUE3MEYtQjIxMjhCM0EyQzZBIn0.f3daVM-MZy8idhskfmafSdcZw6mwIiEzBze7UCZ2V6A",
        "Content-Type": "application/json"
    }
    body = {
      "offeringId": "wah-999",
      "trainingStandardKey": "WAH-10083",
      "deliveryMethod": "in-person",
      "courseName": "Working At Heights",
      "seatsRemaining": 5,
      "contactForPricing": True,
      "price": 100,
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
          "start": "2023-09-05T10:30:00.000Z",
          "end": "2023-09-05T12:00:00.000Z"
        }
      ],
      "externalRegistrationUrl": "https://training-provider.com/reserve-seats/10012",
      "virtualClassUrl": "https://virtual-class-example.com/10001"
    }
    response = requests.post(url, json=body, headers=headers)
    print(response.status_code)  # 204
    print(response.text)  # print(response.json())
    return response.text
# ADD - learning record
# Creating a class using API
# Looking for the same class created by API - same date from the list
# View classroom > submitted records
def api_07_add_learning_record_98393():
    print('07_add_learning_record')
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/LearningRecord"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwia2V5IjoiRTkzM0QxQjMtMzQwNC00RUI1LUE3MEYtQjIxMjhCM0EyQzZBIn0.f3daVM-MZy8idhskfmafSdcZw6mwIiEzBze7UCZ2V6A",
        "Content-Type": "application/json"
    }
    body = {
      "learningRecordId": "4108123e-7f35-4097-928a-5bccd5fe4111",
      "trainingStandardKey": "WAH-10083",
      "completionDate": "2023-09-05T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "wah-999",  # Need to match the ID of the class generated using the API's ClassOffering endpoint
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






# Negative scenarios
# DELETE - online offering - offeringId, Result - Course, ElectronicAddressOwnership, & ElectronicAddress - deleted
def api_08_negative_delete_online_offering_98391():
    print('01_delete_online_offerings')
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/ClassOffering"  # YOUR OFFERING ID HERE
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwia2V5IjoiRTkzM0QxQjMtMzQwNC00RUI1LUE3MEYtQjIxMjhCM0EyQzZBIn0.f3daVM-MZy8idhskfmafSdcZw6mwIiEzBze7UCZ2V6A",
        "Content-Type": "application/json; charset=utf-8"
    }
    body = {
      "offeringId": "ae555337-ca58-46a1-9471-a323a3dbdc85"
    }
    response = requests.delete(url, json=body, headers=headers)
    print(response.status_code)  # 204
    print(response.text)  # print(response.json())
    return response.text
# UPDATE - online offering
def api_09_negative_update_online_offering_98387():
    print('02_update_online_offerings')
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/ClassOffering"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwia2V5IjoiRTkzM0QxQjMtMzQwNC00RUI1LUE3MEYtQjIxMjhCM0EyQzZBIn0.f3daVM-MZy8idhskfmafSdcZw6mwIiEzBze7UCZ2V6A",
        "Content-Type": "application/json"
    }
    body = {
      "courseName": "Working At Heights E-Learning",
      "price": 100,
      "courseDuration": 2.5,
      "externalRegistrationUrl": "https://trainingproviderreservationsystem/register"
    }
    response = requests.patch(url, json=body, headers=headers)
    print(response.status_code)  # 204
    print(response.text)  # print(response.json())
    return response.text
# ADD - online offering
def api_10_negative_add_online_offering_98383():
    print('03_add_online_offerings')
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/OnlineOffering"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwia2V5IjoiRTkzM0QxQjMtMzQwNC00RUI1LUE3MEYtQjIxMjhCM0EyQzZBIn0.f3daVM-MZy8idhskfmafSdcZw6mwIiEzBze7UCZ2V6A",
        "Content-Type": "application/json"
    }
    body = {
      "offeringId": "wah-111",
      "trainingStandardKey": "WAH-E-B-O",
      "courseName": "Working At Heights",
      "price": 100,
      "courseDuration": 2.5,
      "externalRegistrationUrl": "https://trainingproviderreservationsystem/register"
    }
    response = requests.post(url, json=body, headers=headers)
    print(response.status_code)  # 204
    print(response.text)  # print(response.json())
    return response.text
# DELETE - class offering
def api_11_negative_delete_class_offering_98377():
    print('04_delete_class_offerings')
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/OnlineOffering"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwia2V5IjoiRTkzM0QxQjMtMzQwNC00RUI1LUE3MEYtQjIxMjhCM0EyQzZBIn0.f3daVM-MZy8idhskfmafSdcZw6mwIiEzBze7UCZ2V6A",
        "Content-Type": "application/json; charset=utf-8"
    }
    body = {
      "offeringId": "external-class-id"
    }
    response = requests.delete(url, json=body, headers=headers)
    print(response.status_code)  # 204
    print(response.text)  # print(response.json())
    return response.text
# UPDATE - class offering
def api_12_negative_update_class_offering_98372():
    print('05_update_class_offerings')
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/OnlineOffering"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwia2V5IjoiRTkzM0QxQjMtMzQwNC00RUI1LUE3MEYtQjIxMjhCM0EyQzZBIn0.f3daVM-MZy8idhskfmafSdcZw6mwIiEzBze7UCZ2V6A",
        "Content-Type": "application/json"
    }
    body = {
      "courseName": "Working At Heights",
      "seatsRemaining": 5,
      "contactForPricing": True,
      "price": 100,
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
          "start": "2018-11-21T10:30:00.000Z",
          "end": "2018-11-21T12:00:00.000Z"
        }
      ],
      "externalRegistrationUrl": "https://training-provider.com/reserve-seats/10012",
      "virtualClassUrl": "https://virtual-class-example.com/10001"
    }
    response = requests.patch(url, json=body, headers=headers)
    print(response.status_code)  # 204
    print(response.text)  # print(response.json())
    return response.text
# ADD - class offering
def api_13_negative_add_class_offering_98194():
    print('06_add_class_offering')
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/ClassOffering"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwia2V5IjoiRTkzM0QxQjMtMzQwNC00RUI1LUE3MEYtQjIxMjhCM0EyQzZBIn0.f3daVM-MZy8idhskfmafSdcZw6mwIiEzBze7UCZ2V6A",
        "Content-Type": "application/json"
    }
    body = {
      "offeringId": "wah-999",
      "trainingStandardKey": "WAH-10083",
      "deliveryMethod": "in-person",
      "courseName": "Working At Heights",
      "seatsRemaining": 5,
      "contactForPricing": True,
      "price": 100,
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
          "start": "2023-09-05T10:30:00.000Z",
          "end": "2023-09-05T12:00:00.000Z"
        }
      ],
      "externalRegistrationUrl": "https://training-provider.com/reserve-seats/10012",
      "virtualClassUrl": "https://virtual-class-example.com/10001"
    }
    response = requests.post(url, json=body, headers=headers)
    print(response.status_code)  # 204
    print(response.text)  # print(response.json())
    return response.text
# ADD - learning record
# Creating a class using API
# Looking for the same class created by API - same date from the list
# View classroom > submitted records
def api_14_negative_add_learning_record_98393():
    print('07_add_learning_record')
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/LearningRecord"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwia2V5IjoiRTkzM0QxQjMtMzQwNC00RUI1LUE3MEYtQjIxMjhCM0EyQzZBIn0.f3daVM-MZy8idhskfmafSdcZw6mwIiEzBze7UCZ2V6A",
        "Content-Type": "application/json"
    }
    body = {
      "learningRecordId": "4108123e-7f35-4097-928a-5bccd5fe4111",
      "trainingStandardKey": "WAH-10083",
      "completionDate": "2023-09-05T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "wah-999",  # Need to match the ID of the class generated using the API's ClassOffering endpoint
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

