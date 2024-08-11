import os

def check_config_file():
    current_directory = os.getcwd()  # 获取当前工作目录

    # 拼接文件路径
    file_path = os.path.join(current_directory, 'config.json')

    # 判断文件是否存在
    if os.path.exists(file_path):
        return True
    else:
        return False
