from os import getcwd, chdir


def get_parent_path(path):
    switch = False
    new_path = ""
    for char in reversed(path):
        if char == '\\':
            switch = True
        if switch:
            new_path += char
    return new_path[::-1]

print(getcwd())
print(get_parent_path(getcwd()))


