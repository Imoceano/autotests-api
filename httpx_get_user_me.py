import httpx

#Post запрос на логин.
login_response_payloads = {
    "email": "TestUserTask@gmail.com",
    "password": "Qwerty123"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_response_payloads)
login_request_data = login_response.json()

print("Auth response:", login_response.status_code)
print(login_request_data)


#get запрос на получение инфы об авторизованном пользователе по accessToken, взятого из post запроса на логин.

access_token = f"Bearer {login_request_data['token']['accessToken']}"
headers = {"Authorization": access_token }

get_user_me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

print(get_user_me_response.status_code)
print(get_user_me_response.json())
