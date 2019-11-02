from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from tkinter.filedialog import askopenfilename

key = b'\xfc\x9d\xcd\xe8%\xd5\xebkV\\I\xf8\xb1w]\xf5@\x98\x82!vW\x17\xad\x17\x82\x02p\xacl\xa9\x1f'
#Kann jetzt auch bytes richtig verschlüsseln und deschlüsseln


def encrypt(key, path):
    with open(path, "rb")as f:
        msg = f.read()
    if type(msg) == bytes:
        pass
    else:
        msg = msg.encode()
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted_message = cipher.encrypt(pad(msg, AES.block_size))
    with open(path, "wb")as f:
        f.write(cipher.iv)
        f.write(encrypted_message)


def decrypt(key, path):
    with open(path, "rb")as f:
        iv = f.read(16)
        ciphered_data = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    original_date = unpad(cipher.decrypt(ciphered_data), AES.block_size)
    return original_date


path = askopenfilename()

encrypt(key, path)
x = decrypt(key, path)

if type(x) == bytes:
    mode = "wb"
else:
    mode = "w"
with open(path, mode)as f:
   f.write(x)
