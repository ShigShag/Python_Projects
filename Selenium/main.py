from selenium import webdriver
from time import sleep
driver = webdriver.Firefox(executable_path=r'G:\Python_Projects\Selenium\geckodriver.exe')

driver.get("https://www.google.com/xhtml")

sleep(3)

search_field = driver.find_element_by_class_name("gLFyf gsfi")
search_field.send_keys("youtube")
search_field.submit()


#driver.quit()
