cmd = "-batch -h start explorer"
if "-batch" in cmd:

    if "-e" in cmd:
        executed = False
    if "-s" in cmd:
        startup = True
    if "-h" in cmd:
        hide_file = True
        cmd = cmd.replace("-batch ", "")
        cmd = cmd.replace("-h ", "")
print(cmd)