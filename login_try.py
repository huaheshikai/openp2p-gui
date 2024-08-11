import login_auth
import login_token


def login(user, passwd):
    # 使用 login_to_auth 进行认证
    login_successful, auth = login_auth.login_to_auth(user, passwd)
    if login_successful:
        # 使用 login_to_token 获取令牌
        login_successful_token, token = login_token.login_to_token(auth)
        if login_successful_token:
            print("登陆成功")
            return True, auth, token
        else:
            print("登陆失败")
            print("请检查用户名和密码")
            return False, None, None