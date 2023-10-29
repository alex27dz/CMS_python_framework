import time
import pytest
import requests
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import api

'''
* Latency Testing - To measure the time it takes for the API to respond to requests, Script Description: Records the time it takes to receive a response for each API request.
* Data Validation -
* Volume Testing - To assess how a system handles a large volume of data. This type of testing helps evaluate how the system manages data storage, processing, and retrieval when dealing with a substantial amount of data. It aims to identify potential issues such as data overflow, data corruption, and performance degradation.
* Capacity Testing - Objective: To determine the system's ability to handle a specific number of concurrent users or requests, Script Description: Capacity testing assesses the system's capacity to accommodate a predefined number of concurrent users or requests while maintaining optimal performance. This test aims to establish the system's limitations and understand how it responds under different levels of load, checking its scalability with increased resources.
* Stress Testing - To evaluate the system's behavior at or beyond its expected capacity and identify breaking points, Script Description: Stress testing involves subjecting the system to loads that significantly exceed its expected capacity. This type of testing pushes the system to its limits, seeking to uncover its weaknesses, bottlenecks, and potential failure points. The goal is to understand how the system behaves when dealing with extreme loads and whether it can recover gracefully after high-stress scenarios.
* Load Testing - To measure how the system behaves under expected load conditions, Script Description: Load testing simulates typical user loads or requests to assess the system's performance under standard usage scenarios, This test focuses on evaluating whether the system consistently meets predefined performance criteria, including response times, resource utilization, and throughput. It aims to ensure a reliable and satisfactory user experience under expected loads.
* Throughput Testing - To assess the number of requests the API can process within a specific time frame, Script Description: Measures how many requests the API can handle in a given time period.
* Endurance Testing - Evaluate the API's performance over an extended period to check for memory leaks, resource consumption, and performance degradation
* Spike Testing - Assess how the API performs when subjected to sudden and extreme changes in load or traffic
* Scalability Testing - Test how the API scales with an increase in resources, such as servers or nodes, to accommodate growing traffic
* Reliability Testing - Evaluate the API's ability to handle requests over an extended period without failure.
'''


# Data validation
def api_01_data_delete_online_offering_98391():
    print('01_data_delete_online_offering')
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
def api_02_data_update_online_offering_98387():
    print('02_data_update_online_offering')
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
def api_03_data_add_online_offering_98383():
    print('03_data_add_online_offering')
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
def api_04_data_delete_class_offering_98377():
    print('04_data_delete_class_offering')
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
def api_05_data_update_class_offering_98372():
    print('05_data_update_class_offering')
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
def api_06_data_add_class_offering_98194():
    print('06_data_add_class_offering')
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
def api_07_data_add_learning_record_98393():
    print('07_data_add_learning_record')
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


# Latency
def api_08_response_delete_online_offering_98391():
    print('08_response_delete_online_offering')
    num_requests = 10  # Number of requests to send for testing
    max_response_time = 0
    total_response_time = 0
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/ClassOffering"  # YOUR OFFERING ID HERE
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwia2V5IjoiRTkzM0QxQjMtMzQwNC00RUI1LUE3MEYtQjIxMjhCM0EyQzZBIn0.f3daVM-MZy8idhskfmafSdcZw6mwIiEzBze7UCZ2V6A",
        "Content-Type": "application/json; charset=utf-8"
    }
    body = {
      "offeringId": "ae555337-ca58-46a1-9471-a323a3dbdc85"
    }
    for i in range(num_requests):
        start_time = time.time()
        response = requests.delete(url, json=body, headers=headers)
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
def api_09_response_update_online_offering_98387():
    print('09_response_update_online_offering')
    num_requests = 10  # Number of requests to send for testing
    max_response_time = 0
    total_response_time = 0
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
def api_10_response_add_online_offering_98383():
    print('10_response_add_online_offering')
    num_requests = 10  # Number of requests to send for testing
    max_response_time = 0
    total_response_time = 0
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
def api_11_response_delete_class_offering_98377():
    print('11_response_delete_class_offering')
    num_requests = 10  # Number of requests to send for testing
    max_response_time = 0
    total_response_time = 0
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/OnlineOffering"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwia2V5IjoiRTkzM0QxQjMtMzQwNC00RUI1LUE3MEYtQjIxMjhCM0EyQzZBIn0.f3daVM-MZy8idhskfmafSdcZw6mwIiEzBze7UCZ2V6A",
        "Content-Type": "application/json; charset=utf-8"
    }
    body = {
      "offeringId": "external-class-id"
    }
    for i in range(num_requests):
        start_time = time.time()
        response = requests.delete(url, json=body, headers=headers)
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
def api_12_response_update_class_offering_98372():
    print('12_response_update_class_offering')
    num_requests = 10  # Number of requests to send for testing
    max_response_time = 0
    total_response_time = 0
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
def api_13_response_add_class_offering_98194():
    print('13_response_add_class_offering')
    num_requests = 10  # Number of requests to send for testing
    max_response_time = 0
    total_response_time = 0
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
def api_14_response_add_learning_record_98393():
    print('14_response_add_learning_record')
    num_requests = 10  # Number of requests to send for testing
    max_response_time = 0
    total_response_time = 0
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
def api_15_response_times():
    print('15_response_times')
    num_requests = 10  # Number of requests to send for testing
    max_response_time = 0
    total_response_time = 0
    url = "https://intra.stage.apps.labour.gov.on.ca/api-facade-qa/ClassOffering"  # YOUR OFFERING ID HERE
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwia2V5IjoiRTkzM0QxQjMtMzQwNC00RUI1LUE3MEYtQjIxMjhCM0EyQzZBIn0.f3daVM-MZy8idhskfmafSdcZw6mwIiEzBze7UCZ2V6A",
        "Content-Type": "application/json"
    }
    for i in range(num_requests):
        start_time = time.time()
        response = requests.get(url, headers=headers)
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


