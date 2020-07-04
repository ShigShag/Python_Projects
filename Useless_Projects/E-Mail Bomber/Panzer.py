import threading
import sys
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

csv_path = r"G:\Python_Projects\Useless_Projects\E-Mail Bomber\specs.csv"
target_address = r"LuckyLuke1200@gmx.de"

counter = 0

def get_csv(path):
    return_array = []
    with open(path, "r")as f:
        info = csv.reader(f)
        next(info)
        for line in info:
            return_array.append(line)

    return return_array

def panzer(array, driver):
    for address, before, name_, class_, id_ in array:

        driver.get(address)

        if before is not None:
            if before == "0":
                pass
            elif before == "1":
                first, second = class_.split("°")
                element = driver.find_element_by_class_name(first)
                element.click()
            elif before == "2":
                pass
            else:
                continue


        try:

            if name_:
                element = driver.find_element_by_name(name_)
                element.clear()
                element.send_keys(target_address)
                element.send_keys(Keys.RETURN)

            elif class_:
                element = driver.find_element_by_class_name(class_)
                element.clear()
                element.send_keys(target_address)
                element.send_keys(Keys.RETURN)

            elif id_:
                element = driver.find_element_by_id(id_)
                element.clear()
                element.send_keys(target_address)
                element.send_keys(Keys.RETURN)

        except NoSuchElementException:
            continue


def initialize(array):
    gecko1 = webdriver.Firefox(executable_path=r"G:\Python_Projects\Selenium\geckodriver.exe")
    gecko2 = webdriver.Firefox(executable_path=r"G:\Python_Projects\Selenium\geckodriver.exe")

    gecko1.implicitly_wait(5)
    gecko2.implicitly_wait(5)

    first, second = split_list(array)

    threads = [threading.Thread(target=panzer, args=(first, gecko1)), threading.Thread(target=panzer, args=(second, gecko2))]

    for thread in threads:
        thread.daemon = True
        thread.start()

    for thread in threads:
        thread.join()

    #gecko1.quit()
    #gecko2.quit()


def split_list(l):
    mid = len(l) // 2
    return l[:mid], l[mid:]

# address name class id
initialize(get_csv(csv_path))
