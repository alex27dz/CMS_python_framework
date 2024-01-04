import time
import pytest
import requests
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import api
'''
* Latency Testing - To measure the time it takes for the API to respond to requests, Script Description: Records the time it takes to receive a response for each API request.
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



