import requests


def login_to_token(auth):
    post_url = "https://console.openp2p.cn/api/v1/user/profile"
    headers = {
        "Authorization": auth
    }
    post_response = requests.post(post_url, headers=headers)

    if post_response.status_code == 200:
        response_data = post_response.json()
        error_code = response_data.get("error")
        login_token = response_data.get("profile", {}).get("token")

        if error_code == 0:  # 假设error_code为0表示登录成功
            return True, login_token
        else:
            return False, None