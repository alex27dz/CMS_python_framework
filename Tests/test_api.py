import requests
import api
import pytest

def test_get_user_data():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    print(response.status_code)  # 200 success
    data = response.json()
    print(data)
    print(data['username'])
    assert response.status_code == 200
    assert data["username"] == "Bret"
def test_post_with_authentication():
    url = "https://api.example.com/resource"
    headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}
    data = {"key": "value"}
    response = requests.post(url, json=data, headers=headers)

    print(response.status_code)  # 200 success
    data = response.json()
    print(data)

    assert response.status_code == 201
    assert data["message"] == "Success"
def test_error_handling():
    response = requests.get("https://jsonplaceholder.typicode.com/nonexistent")
    assert response.status_code == 404
    error_data = response.json()
    assert error_data["message"] == "Resource not found"
def test_put_request():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    data = {"title": "Updated Title"}

    response = requests.put(url, json=data)

    assert response.status_code == 200
    updated_post = response.json()
    assert updated_post["title"] == "Updated Title"
def test_delete_request():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.delete(url)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["message"] == "Post deleted successfully"
def test_create_post_no_authentication():
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {
        "title": "New alex Post",
        "body": "This is a new post.",
        "userId": 1
    }
    response = requests.post(url, json=data)

    print(response.status_code)
    assert response.status_code == 201
    response_data = response.json()
    print(response_data)
    assert response_data["title"] == "New alex Post"
    assert response_data["body"] == "This is a new post."
    assert response_data["userId"] == 1

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




