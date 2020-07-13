import os
import shutil
from sys import exit


def main():
    destination_folder = "F:/"
    os.chdir(destination_folder)
    cpp_name = "C++ PROJECTS"
    c_name = "C PROJECTS"
    create_save_folders(cpp_name, c_name)
    move_directories(destination_folder, cpp_name, c_name)


def move_directories(origin_path, cpp_path, c_path):
    for name in os.listdir(origin_path):
        try:
            for files in os.listdir(name):
                if files.endswith(".c"):
                    shutil.move(name, c_path)
                    break
                elif files.endswith(".cpp"):
                    shutil.move(name, cpp_path)
                    break
        except PermissionError:
            continue

def create_save_folders(name_cpp, name_c):
    try:
        os.mkdir(name_cpp)
        os.mkdir(name_c)
    except OSError:
        pass


if __name__ == "__main__":
    exit(main())