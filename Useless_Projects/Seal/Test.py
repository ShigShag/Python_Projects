with open("Test.exe", "rb")as f:
    x = f.read()

with open("test1.exe", "wb+")as f:
    f.write(x)