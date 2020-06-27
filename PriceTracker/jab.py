import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

duration = 4
icon = "radon_logo_2019_black.ico"
# JAB 10.0 PRICE TRACKER
try:
    with open("price_tracker.txt", "r")as f:
        old_track = f.readlines()
except (PermissionError, FileNotFoundError):
    pass

url = "https://www.bike-discount.de/de/kaufen/radon-jab-10.0-912961"
source = requests.get(url).text
soup = BeautifulSoup(source, "lxml")

price = soup.find(class_="price")
price = price.contents[0].replace(",- €", "")

try:
    with open("price_tracker.txt", "w")as f:
        f.write(price)
except (PermissionError, FileNotFoundError):
    pass

toaster = ToastNotifier()
if price != old_track[0]:
    toaster.show_toast("PRICE OF RADON JAB 10.0 CHANGED TO:", price + "€\n", icon_path=icon, duration=duration)


# JAB 10.0 PRICE TRACKER


# JAB 10.0 HD SOLD OUT TRACKER

url = "https://www.radon-bikes.de/mountainbike/fullsuspension/jab/jab-100-hd-2020/"
source = requests.get(url).text
soup = BeautifulSoup(source, "lxml")

sold_out = soup.find(class_="a-badge a-badge--soldOut a-badge--soldOut-large a-badge--right-upperhalf")
if not sold_out:
    price = soup.find(class_="m-bikedetail__price--active")

    toaster.show_toast("RADON JAB 10.0 HD NOT SOLD OUT ANYMORE", price.contents[0], icon_path=icon, duration=duration)

# JAB 10.0 HD SOLD OUT TRACKER


