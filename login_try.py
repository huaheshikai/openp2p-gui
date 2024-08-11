import login_auth
import login_token
def login():
username = "2813837083"
password = "xdC.fM8rWhQ2T"
login_successful, auth = login_auth.login_to_auth(username, password)
# print(login_successful, auth)
    if login_successful:
        login_successful_token, token = login_token.login_to_token(auth)
        # print(login_successful_token, token)
        if login_successful_token:
            return True
        else:
            return False
    else:
        print("登录失败，请联系作者!")
        return False