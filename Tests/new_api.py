import requests

def postman_API():
    print('Add Learning Record API')
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
    print(response.json())
    print(response.text)


postman_API()



