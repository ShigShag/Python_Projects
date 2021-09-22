import sys
from collections import Counter
from os.path import split

def letter_frequency(s):

    # Remove digits and special characters from string
    s = ''.join(filter(lambda x: x.isalnum() and not x.isdigit(), s))

    count = Counter(s).items()
    c = sorted(count, key=lambda x: (x[1]), reverse=True)

    return c

def main():

    if len(sys.argv) < 2:
        tail = split(sys.argv[0])
        print(f"Usage: {tail[1]} [Ascii roman digit]")
        return 1

    print(letter_frequency(sys.argv[1]))

if __name__ == '__main__':
    sys.exit(main())