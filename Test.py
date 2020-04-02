class Settings:
    # Variables
    cycles = 10
    string_path = r"G:\Python_Projects\Constants\String123.txt"


with open(__file__, "r+")as file:
    content = file.read()

new_string = r"G:\Python_Projects\Constants\String123.txt"
content = content.replace(f'string_path = r"{Settings.string_path}"', f'string_path = r"{new_string}"')

with open(__file__, "w")as file:
    file.write(content)