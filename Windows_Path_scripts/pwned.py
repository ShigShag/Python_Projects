import requests
import hashlib
from sys import argv, exit


def get_count(pwd):
    sha1pwd = hashlib.sha1(pwd.encode('utf-8')).hexdigest().upper()
    head, tail = sha1pwd[:5], sha1pwd[5:]

    r = requests.get("https://api.pwnedpasswords.com/range/{}".format(head))
    hashes = (line.split(':') for line in r.text.splitlines())
    for h, count in hashes:
        if h == tail:
            return sha1pwd, count
    return sha1pwd, 0


def main(pwd):
    try:
        import requests
    except ModuleNotFoundError:
        print("pip install requests")
        exit()

    sha1, count = get_count(pwd)
    print("{} was found {} times [HASH: {}]".format(pwd, count, sha1))


if __name__ == '__main__':
    exit(main(argv[1]))
