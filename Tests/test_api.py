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




