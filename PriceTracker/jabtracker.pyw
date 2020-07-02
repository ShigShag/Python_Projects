import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

duration = 4
icon = r"G:\Python_Projects\PriceTracker\radon_logo_2019_black.ico"
price_file = r"G:\Python_Projects\PriceTracker\price_tracker.txt"
size_file = r"G:\Python_Projects\PriceTracker\sizetracker.txt"

# JAB 10.0 PRICE TRACKER
try:
    with open(price_file, "r")as f:
        old_track = f.readlines()
except (PermissionError, FileNotFoundError):
    pass

url = "https://www.bike-discount.de/de/kaufen/radon-jab-10.0-912961"
source = requests.get(url).text
soup = BeautifulSoup(source, "lxml")

price = soup.find(class_="price")
price = price.contents[0].replace(",- €", "")

try:
    with open(price_file, "w")as f:
        f.write(price)
except (PermissionError, FileNotFoundError):
    pass

toaster = ToastNotifier()
if price != old_track[0]:
    toaster.show_toast("PRICE OF RADON JAB 10.0 CHANGED TO:", price + "€", icon_path=icon, duration=duration)

# JAB 10.0 PRICE TRACKER

# JAB 10.0 SIZE TRACKER

source = requests.get("https://www.bike-discount.de/de/kaufen/radon-jealous-8.0-912808").text
soup = BeautifulSoup(source, "lxml")
x = soup.find_all("data-vartext", class_="vselect-type2")
size = soup.find(class_="vselect-type2")
size_amount = str(size.prettify().count("class") - 1)

with open(size_file, "r")as f:
    prev_size_amount = f.read()

if prev_size_amount == size_amount:
    with open(size_file, "w")as f:
        f.write(size_amount)

    size = size.prettify()

    tag = "data-vartext"

    a = size.find(tag)
    b = size[a + len(tag):].find(tag)

    print(size)
    print(size[a:])
    print(size[b:])




#import sys
#sys.exit()


# JAB 10.0 SIZE TRACKER



# JAB 10.0 HD SOLD OUT TRACKER

url = "https://www.radon-bikes.de/mountainbike/fullsuspension/jab/jab-100-hd-2020/"
source = requests.get(url).text
soup = BeautifulSoup(source, "lxml")

sold_out = soup.find(class_="a-badge a-badge--soldOut a-badge--soldOut-large a-badge--right-upperhalf")
if not sold_out:
    price = soup.find(class_="m-bikedetail__price--active")

    toaster.show_toast("RADON JAB 10.0 HD NOT SOLD OUT ANYMORE", price.contents[0], icon_path=icon, duration=duration)






# JAB 10.0 HD SOLD OUT TRACKER


