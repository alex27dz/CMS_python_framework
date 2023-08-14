import requests
import api
import pytest
'''
Given the user would like to create a learning record using an API
When they access the MLTSD CMS API Learning Records endpoint
Then they can execute a call to create a learning record
And the request headers and parameters should mirror the parameters identified in the documentation link above
When the learner unique id does not exist in the system
Then insert the learning record
When the learner unique id does exist in the system
Then update the learning record
'''

# Add Learning Record API
def get_data_new():
    print('Add Learning Record AP')
    url = "https://private-anon-78376c118a-bluedrop360apiv2network.apiary-mock.com/api-v2/learning-records"
    headers = {
        "Content-Type": "application/json",
    }
    body = {
      "learningRecordId": "4108123e-7f35-4097-928a-5bccd5fe4111",
      "trainingStandardKey": "WAH-E-B",
      "completionDate": "2018-11-21T22:38:15.000Z",
      "networkKey": "pro-34616",
      "externalClassId": "external-class-111",
      "instructorNames": "Jane Doe; Dave Weir",
      "evaluatorNames": "John Smith",
      "learner": {
        "uniqueId": "user-121",
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
    # print(response.text)
get_data_new()


# API 1

# API 2

# API 3

# API 4

# API 5

