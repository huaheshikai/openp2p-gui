import subprocess
import os


def install_openp2p(node_name, token):
    command = f'openp2p -d -node {node_name} -token {token}'
    try:
        if os.name == 'nt':  # 检查是否为Windows系统
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       startupinfo=startupinfo)
        else:
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        print("正在开服请稍等........")
        print("按Ctrl+C退出当前程序")

        try:
            # 逐行读取输出并实时显示
            for stdout_line in iter(process.stdout.readline, b''):
                print(stdout_line.decode('utf-8').strip())  # 打印每行输出，strip() 去除换行符

        except KeyboardInterrupt:
            process.terminate()
            process.wait()

        stdout, stderr = process.communicate()

        if stdout:
            print(stdout.decode('utf-8').strip())  # 打印子进程的标准输出
        if stderr:
            print(stderr.decode('utf-8').strip())  # 打印子进程的标准错误

    except subprocess.CalledProcessError as e:
        print(f"启动失败，错误信息: {e}")
        if e.stderr:
            print(e.stderr.decode('utf-8'))  # 解码 stderr 输出
