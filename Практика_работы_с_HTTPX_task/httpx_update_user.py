import httpx
from tools.fakers import get_random_email
from tools.fakers import get_random_first_name
from tools.fakers import get_random_last_name
from tools.fakers import get_random_middle_name
from tools.fakers import get_random_password

#создание пользователя
create_user_payloads = {
    "email": get_random_email(),
    "password": get_random_password(),
    "lastName": get_random_last_name(),
    "firstName": get_random_first_name(),
    "middleName": get_random_middle_name()
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payloads)
create_user_request_data = create_user_response.json()

if create_user_response.status_code == 200:
    print(f"Пользователь с email {create_user_payloads['email']} - успещно создан")
else:
    print("Ошибка при создании пользователя. Статус код: ", create_user_response.status_code)

print(f"Create User. Status code: ",create_user_response.status_code)
print(f"Create User request:", create_user_request_data)




#авторизация пользователя
auth_email_data = create_user_payloads["email"]
auth_password_data = create_user_payloads["password"]

auth_payloads = {
    "email": auth_email_data,
    "password": auth_password_data
}

login_user_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=auth_payloads)
login_request_data = login_user_response.json()

if login_user_response.status_code == 200:
    print(f"Пользователь с email {auth_email_data} - успещно авторизован")
else:
    print("Ошибка при авторизации пользователя. Статус код: ", login_user_response.status_code)

print(f"Login User. Status code: ", login_user_response.status_code)
print(f"Login User request: ", login_request_data)



#редактирование пользователя
new_first_name = get_random_first_name()
new_middle_name = get_random_middle_name()
new_last_name = get_random_last_name()
new_email = get_random_email()

edit_users_payloads = {
    "email": new_email,
    "lastName": new_last_name,
    "firstName": new_first_name,
    "middleName": new_middle_name
}

access_token = f"Bearer {login_request_data['token']['accessToken']}"
headers = {"Authorization": access_token }
user_id = create_user_response.json()['user']['id']



edit_user_response = httpx.patch(f"http://localhost:8000/api/v1/users/{user_id}", headers=headers, json=edit_users_payloads)

if edit_user_response.status_code == 200:
    print(f"Пользователь с user_id {user_id} - успещно изменен")
else:
    print("Ошибка при изменении пользователя. Статус код: ", edit_user_response.status_code)

print("Edit User status code: ", edit_user_response.status_code)
print("Edit user request: ", edit_user_response.json())