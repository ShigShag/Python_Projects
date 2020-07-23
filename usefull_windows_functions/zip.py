import zipfile

# normal
"""
with zipfile.ZipFile("files.zip", "w") as my_zip:
    my_zip.write("a.pdf")
    my_zip.write("b.txt")
    my_zip.write("c.odt")
´"""


# compressed
'''with zipfile.ZipFile("files.zip", "w", compression=zipfile.ZIP_DEFLATED) as my_zip:
    my_zip.write("a.pdf")
    my_zip.write("b.txt")
    my_zip.write("c.odt")'''

# read
with zipfile.ZipFile("files.zip", "r")as my_zip:
    print(my_zip.namelist())
    # files = directory to store extracted stuff
    my_zip.extractall("files")