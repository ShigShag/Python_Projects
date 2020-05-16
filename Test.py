from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from sys import exit


class Bomber:

    def __init__(self, mail):
        self.driver = webdriver.Firefox(executable_path=r'G:\Python_Projects\Selenium\geckodriver.exe')
        self.target_address = mail
        self.counter = 0
        self.driver.implicitly_wait(10)

    def start_bombing(self, delay=0, show_counter=0):
        self.call("https://www.techbook.de/newsletter", name="inp_3",show_counter=show_counter)
        sleep(delay)
        self.call("https://snacks.robinhood.com/", class_c="css-r92b85",show_counter=show_counter)
        sleep(delay)
        self.call("https://www.myhomebook.de/newsletter", name="inp_3",show_counter=show_counter)
        sleep(delay)
        self.call("https://www.morningbrew.com/", id="subscription-email-form-input",show_counter=show_counter)
        sleep(delay)
        self.call("https://nextdraft.com/", id="mce-EMAIL",show_counter=show_counter)
        sleep(delay)
        self.call("https://moz.com/moztop10#confirmation", id="email-379ffa8c-772e-4b7b-9c22-47d60e0db419",show_counter=show_counter)

    def call(self, site, name='', class_c='', id='', show_counter=0):
        self.driver.get(site)
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

    def quit_driver(self):
        self.driver.quit()


def main():
    target = Bomber("luccat@gmail.com")
    target.start_bombing(show_counter=1)
    input()
    target.quit_driver()



if "__main__" == __name__:
    exit(main())