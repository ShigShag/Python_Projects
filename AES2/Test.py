file_name = "12334"

try:
    try:
        file = open(file_name, "rb")
        data = file.read()
    except NameError:
        print("File not Found")
finally:
    file.close()