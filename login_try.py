import login_auth
import login_token


def login():
    username = input("请输入用户名：")
    password = input("请输入密码：")

    try:
        # 使用 login_to_auth 进行认证
        login_successful, auth = login_auth.login_to_auth(username, password)
        if login_successful:
            # 使用 login_to_token 获取令牌
            login_successful_token, token = login_token.login_to_token(auth)
            if login_successful_token:
                print("以默认设置登陆成功")
                return True, auth, token
            else:
                return False, None, None
        else:
            return False, None, None
    except Exception as e:
        # 捕获并处理所有异常
        print(f"发生错误: {e}")
        return False, None, None
