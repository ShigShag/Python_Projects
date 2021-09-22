import sys
from os.path import split

roman_digits = {
 'I': 1, 'IV': 4,
 'V': 5, 'IX': 9,
 'X': 10, 'XL': 40,
 'L': 50, 'XC': 90,
 'C': 100, 'CD': 400,
 'D': 500, 'CM': 900,
 'M': 1000
}

def RomanToInt(s):
    value = 0
    index = 0
    for r_digit in reversed(roman_digits):
        while s[index:index + len(r_digit)] == r_digit:
            value += roman_digits[r_digit]
            index += len(r_digit)
    return value

def main():

    if len(sys.argv) < 2:
        tail = split(sys.argv[0])
        print(f"Usage: {tail[1]} [Ascii roman digit]")
        return 1

    integer = RomanToInt(sys.argv[1])
    print(integer)

if __name__ == '__main__':
    sys.exit(main())