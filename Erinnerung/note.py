from sys import argv, exit
path = "F:\Python_Projects\Erinnerung\stats.txt"
try:
    argv[1]
except IndexError:
    exit()

if argv[1] == "add":
    with open(path, "a")as f:
        for msg in argv[2:]:
            f.write(msg + "\n")
    print("done")

elif argv[1] == "delete" or argv[1] == "del" or argv[1] == "rem":
    with open(path, "r")as f:
        content = f.readlines()

    for i in argv[2:]:
        try:
            content.pop(int(i))
        except (TypeError, ValueError, IndexError):
            print(f"Error with paramter: '{i}'")

    with open(path, "w")as f:
        f.writelines(content)

    print("done")

elif argv[1] == "list" or argv[1] == "ls" or argv[1] == "dir":
    with open(path, "r")as f:
        content = f.readlines()

    counter = 0

    for i in content:
        print(f"[{counter}]\t{i}")
        counter += 1

else:
    print("Wrong arguments")