from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox(executable_path=r'G:\Python_Projects\Selenium\geckodriver.exe')

driver.implicitly_wait(50)

def news1(site, email):
    driver.get(site)
    search = driver.find_element_by_name("inp_3")
    search.clear()
    search.send_keys(email)
    """
    search = driver.find_element_by_name("inp_1")
    search.clear()
    search.send_keys("Lulcy")

    search = driver.find_element_by_name("inp_2")
    search.clear()
    search.send_keys("Traice")
    """
    search = driver.find_element_by_name("submit")
    search.send_keys(Keys.RETURN)


def news2(site, email):
    driver.get(site)
    search = driver.find_element_by_name("e")
    search.send_keys(email)
    search.send_keys(Keys.RETURN)


def news3(site, email):
    driver.get(site)
    search = driver.find_element_by_class_name("css-r92b85")
    search.send_keys(email)
    search.send_keys(Keys.RETURN)

"""
news1("https://www.techbook.de/newsletter", "ugalhoma@gmail.com")
sleep(2)
news1("https://www.myhomebook.de/newsletter", "schlusseldieb@gmail.com")
sleep(2)
news2("https://www.ladenzeile.de/", "ugalhoma@gmail.com")"""
#news3("https://snacks.robinhood.com/", "ugalhoma@gmail.com")

# driver.back()
# driver.forward()


def call(site, email, name='', class_c='', id='', amount_to_click=1):
    driver.get(site)
    if name:
        element = driver.find_element_by_name(name)
        element.clear()
        element.send_keys(email)
        element.send_keys(Keys.RETURN)
    elif class_c:
        element = driver.find_element_by_class_name(class_c)
        element.clear()
        element.send_keys(email)
        element.send_keys(Keys.RETURN)
    elif id:
        element = driver.find_element_by_id(id)
        element.clear()
        element.send_keys(email)
        element.send_keys(Keys.RETURN)

email = "luccat@gmail.com"
#call("https://www.techbook.de/newsletter", email, name="inp_3")
#call("https://snacks.robinhood.com/", email, class_c="css-r92b85")
#call("https://www.myhomebook.de/newsletter", email, name="inp_3")
#call("https://www.morningbrew.com/", email, id="subscription-email-form-input")
#call("https://nextdraft.com/", email, id="mce-EMAIL")
#call("https://moz.com/moztop10#confirmation", email, id="email-379ffa8c-772e-4b7b-9c22-47d60e0db419")
input()



driver.quit()
