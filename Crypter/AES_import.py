from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


def encrypt(key, salt, path):
    with open(path, "rb")as f:
        msg = f.read()
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted_message = cipher.encrypt(pad(msg, AES.block_size))
    with open(path, "wb")as f:
        f.write(salt)
        f.write(cipher.iv)
        f.write(encrypted_message)


def decrypt(user_password, path):
    with open(path, "rb")as f:
        salt = f.read(32)
        iv = f.read(16)
        ciphered_data = f.read()
    key = PBKDF2(user_password, salt, dkLen=32)
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    original_date = unpad(cipher.decrypt(ciphered_data), AES.block_size)
    return original_date


def keygen(user_password):
    random_string = "mucj9058tu9q083ut09q53ut905uz8t07z5238790t5h23807t235th9235h8x95,mh589th82htc3ßm509ug908ß3uq9ßc8guq39ß0mgcuq5390u,g59q3g953q08ugßq053ug0ßq3u8tgß0q3tu0qß38ut0ßt5q3t5q34g6543168436g456587g4q653g426q53g42q246g4cg89254qg9494z994j98846m98lk497p9890,78419,m8198794,m96785fmc3jh2t"
    salt = get_random_bytes(32)
    return PBKDF2(user_password + random_string, salt, dkLen=32), salt



