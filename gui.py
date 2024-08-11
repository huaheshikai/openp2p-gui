import login_try
import install_openp2p
import ctypes
import installed
import installed_openp2p
import sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False


def option2():
    print("没写")


def option3():
    print("没写")


def option4():
    print("底层由openp2p项目支持")
    print("项目地址")


def show_menu():
    print("=== 菜单 ===")
    print("1. 开服")
    print("2. 进服")
    print("3. 设置")
    print("4. 关于")
    print("0. 退出")
    print("============")


if __name__ == "__main__":
    if not is_admin():
        print("需要管理员权限，请确认以管理员身份运行此程序！")
        input("按任意键退出...")
        sys.exit()
    while True:
        show_menu()
        choice = input("请输入选项编号: ")
        if choice == "1":
            if installed.check_config_file():
                installed_openp2p.config_openp2p()
            else:
                node_name = input("请输入你的电脑名(六位英文以上可用-连接): ")
                login_success, auth, token = login_try.login()
                print("正在安装p2p")
                install_openp2p.install_openp2p(node_name, token)
        elif choice == "2":
            option2()
        elif choice == "3":
            option3()
        elif choice == "4":
            option4()
        elif choice == "0":
            print("退出程序")
            break
        else:
            print("无效选项，请重新输入")
