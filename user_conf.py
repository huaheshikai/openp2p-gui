import os
from cryptography.fernet import Fernet


def check_user_conf_exists():
    conf_dir = os.path.join(os.getcwd(), 'conf')
    user_conf_path = os.path.join(conf_dir, 'user.conf')
    return os.path.isfile(user_conf_path)


# 生成密钥并保存到文件
def generate_key():
    key = Fernet.generate_key()
    with open(os.path.join('conf', 'key.key'), 'wb') as key_file:
        key_file.write(key)


# 加载密钥
def load_key():
    return open(os.path.join('conf', 'key.key'), 'rb').read()


# 加密数据
def encrypt_data(data, key):
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data


# 保存到user.conf文件
def save_encrypted_user_data(user, passwd):
    conf_dir = os.path.join(os.getcwd(), 'conf')
    if not os.path.exists(conf_dir):
        os.makedirs(conf_dir)

    key_file = os.path.join(conf_dir, 'key.key')
    if not os.path.exists(key_file):
        generate_key()

    key = load_key()
    encrypted_user = encrypt_data(user, key)
    encrypted_passwd = encrypt_data(passwd, key)

    user_conf_path = os.path.join(conf_dir, 'user.conf')
    with open(user_conf_path, 'wb') as file:
        file.write(encrypted_user + b'\n' + encrypted_passwd)


# 解密数据
def decrypt_data(encrypted_data, key):
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data).decode()
    return decrypted_data


# 从user.conf文件读取并解密数据
def load_and_decrypt_user_data():
    conf_dir = os.path.join(os.getcwd(), 'conf')
    user_conf_path = os.path.join(conf_dir, 'user.conf')

    if not os.path.exists(user_conf_path):
        raise FileNotFoundError("user.conf文件不存在")

    key = load_key()

    with open(user_conf_path, 'rb') as file:
        encrypted_user, encrypted_passwd = file.read().split(b'\n')

    user = decrypt_data(encrypted_user, key)
    passwd = decrypt_data(encrypted_passwd, key)

    return user, passwd


# 使用示例
# user = 'example_user'
# passwd = 'example_password'
# save_encrypted_user_data(user, passwd)
#
# loaded_user, loaded_passwd = load_and_decrypt_user_data()
# print(f'用户名: {loaded_user}')# print(f'密码: {loaded_passwd}')
