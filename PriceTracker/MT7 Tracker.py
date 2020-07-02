import requests
from datetime import datetime
from bs4 import BeautifulSoup

source = requests.get("https://www.bike-components.de/de/Magura/MT7-Pro-HC-Carbotecture-v-h-Set-Scheibenbremse-p61249/").text
soup = BeautifulSoup(source, "lxml")

price = soup.find(id="module-product-detail-price").contents[0].replace(" ", "").replace("€", "")


if price is not None:
    path = "G:\Python_Projects\PriceTracker\mt7track.txt"
    time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open(path, "a")as f:
        f.write(time + " " + price + "€\n")
