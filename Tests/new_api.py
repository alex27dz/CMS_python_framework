'''
API requests are the mechanisms by which one software application sends a request to another application's API to perform certain actions or retrieve specific information

Components of an API Request:

* HTTP Method (Request Verb): The HTTP method specifies the type of action you want to perform on the resource. Common methods include:
    * GET: Retrieve data from the server.
    * POST: Send data to the server to create a new resource.
    * PUT: Update an existing resource on the server.
    * DELETE: Delete a resource on the server.

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


Add the APIs here
https://netsdc.visualstudio.com/SDC/_workitems/edit/98391	1	CMS API: Online Offerings - Delete
https://netsdc.visualstudio.com/SDC/_workitems/edit/98387	2	CMS API: Online Offerings - Update (Patch)
https://netsdc.visualstudio.com/SDC/_workitems/edit/98383	3	CMS API: Online Offerings - Add
https://netsdc.visualstudio.com/SDC/_workitems/edit/98377	4	CMS API: Class Offerings - Delete
https://netsdc.visualstudio.com/SDC/_workitems/edit/98372	5	CMS API: Class Offerings - Update (Patch)
https://netsdc.visualstudio.com/SDC/_workitems/edit/98194	6	CMS API: Class Offerings - Add
'''

import requests
import api
import pytest


def postman_API():
    print('Postman API')
    url = "http://postman-echo.com/get"
    headers = {"Content-Type": "application/json"}
    body = {
            "args": {},
            "headers": {
                "x-forwarded-proto": "http",
                "x-forwarded-port": "80",
                "host": "postman-echo.com",
                "x-amzn-trace-id": "Root=1-64e9370b-0ae159ae79b5d3ef3ff1afa2",
                "user-agent": "PostmanRuntime/7.32.3",
                "accept": "*/*",
                "postman-token": "37cf0a76-fa63-4f5e-9565-d370db89298e",
                "accept-encoding": "gzip, deflate, br"
            },
            "url": "http://postman-echo.com/get"
    }

    # sending get request
    response = requests.get(url, json=body, headers=headers)
    print(response.status_code)  # 200 success
    # print(response.json())
    print(response.text)

def add_class_offerings_98194():
    print('api_class_offerings_add')
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
    # print(response.json())
    print(response.text)
    return response.text
# add_class_offerings_98194()

def add_learning_record_api_98393():
    print('Add Learning Record API')
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
    # print(response.json())
    print(response.text)
    return response.text
# add_learning_record_api_98393()















