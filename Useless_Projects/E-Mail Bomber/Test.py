import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
from sys import exit


class Bomber:

    def __init__(self, mail):
        self.driver = webdriver.Firefox(executable_path=r'G:\Python_Projects\Selenium\geckodriver.exe')
        self.target_address = mail
        self.counter = 0
        self.driver.implicitly_wait(20)

    def read_csv_file(self, delay=0, show_counter=1):
        with open("specs.csv", "r")as csv_file:
            content = csv.reader(csv_file)
            next(content)
            for entry in content:
                try:
                    self.call(entry[0], name=entry[1], class_c=entry[2], id=entry[3], show_counter=show_counter)
                except:
                    print("Skipped element!! {}".format(self.counter + 1))
                    self.counter += 1
                    continue
                sleep(delay)
        self.counter = 0

    def call(self, address, name='', class_c='', id='', show_counter=0):
        self.driver.get(address)
        if name:
            element = self.driver.find_element_by_name(name)
            element.clear()
            element.send_keys(self.target_address)
            element.send_keys(Keys.RETURN)

        elif class_c:
            element = self.driver.find_element_by_class_name(class_c)
            element.clear()
            element.send_keys(self.target_address)
            element.send_keys(Keys.RETURN)

        elif id:
            element = self.driver.find_element_by_id(id)
            element.clear()
            element.send_keys(self.target_address)
            element.send_keys(Keys.RETURN)

        if show_counter:
            self.counter += 1
            print(self.counter)

    def special_call(self):
        pass

    def quit_driver(self):
        self.driver.quit()


def main():
    target = Bomber("CowboyBebopopopo@protonmail.com")
    target.read_csv_file()
    target.quit_driver()


if __name__ == "__main__":
    exit(main())
