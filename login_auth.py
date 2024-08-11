import requests


def login_to_auth(username, password):
    url = "https://console.openp2p.cn/api/v1/user/login"
    payload = {"user": username, "password": password}

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        response_data = response.json()
        error_code = response_data.get("error")
        auth = response_data.get("token")

        if error_code == 0:  # 假设error_code为0表示登录成功
            return True, auth
        else:
            return False, error_code
