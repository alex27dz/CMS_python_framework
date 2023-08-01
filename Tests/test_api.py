# api.py (the code you are testing)
import requests
import api

# need apis links and authentication, db information

import pytest
def get_tasks():
    response = requests.get("https://example-api.com/tasks")
    return response.json()
def test_get_tasks_status_code():
    response = api.get_tasks()
    assert response.status_code == 200
def test_get_tasks_data():
    response = api.get_tasks()
    assert "tasks" in response


BASE_URL = "https://example-api.com"
HEADERS = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}  # Replace with your actual access token
def get_tasks():
    response = requests.get(f"{BASE_URL}/tasks", headers=HEADERS)
    return response
def create_task(title):
    data = {"title": title}
    response = requests.post(f"{BASE_URL}/tasks", json=data, headers=HEADERS)
    return response
def update_task(task_id, title):
    data = {"title": title}
    response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=data, headers=HEADERS)
    return response
def delete_task(task_id):
    response = requests.delete(f"{BASE_URL}/tasks/{task_id}", headers=HEADERS)
    return response.status_code
def test_get_tasks_status_code():
    response = get_tasks()
    assert response.status_code == 200
def test_get_tasks_data():
    response = get_tasks()
    assert "tasks" in response.json()
def test_create_task():
    new_task_title = "New Task"
    response = create_task(new_task_title)
    assert response.status_code == 200
    assert response.json()["title"] == new_task_title
def test_update_task():
    task_id = 1
    updated_task_title = "Updated Task"
    response = update_task(task_id, updated_task_title)
    assert response.status_code == 200
    assert response.json()["title"] == updated_task_title
def test_delete_task():
    task_id = 1
    response = delete_task(task_id)
    assert response == 204
