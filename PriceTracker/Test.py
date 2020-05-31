import requests
import csv
from bs4 import BeautifulSoup

def main():
    # read csv file
    with open("stats.csv", "r")as f:
        data = csv.reader(f)

        # Skip description line
        next(data)
        next(data)

        for entry in data:
            show(entry[0], entry[1])


def show(url, tag):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')


    while True:
        price = soup.find(id=tag)
        if price is not None:
            break

        price = soup.find(class_=tag)
        if price is not None:
            break

    if price is None:
        print(f"Error at: {url}")
        return

    print(url)
    print(price)
    return


if __name__ == '__main__':
    main()



