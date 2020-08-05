import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return 0

if __name__ == '__main__':
    print(is_admin())