from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time # for delay


def login(driver):
    username = "drefaeli1"  # <username here>
    password = "baronit"  # <password here>

    # Load page
    driver.get("https://www.instagram.com/accounts/login/")

    # Login
    driver.find_element_by_xpath("//div/input[@name='username']").send_keys(username)
    driver.find_element_by_xpath("//div/input[@name='password']").send_keys(password)
    driver.find_element_by_xpath("//span/button").click()

    # Wait for the login page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "See All")))


def scroll_photos(driver, account):
    # Load account page
    driver.get("https://www.instagram.com/explore/tags/{0}/".format(account))

    tag_name = "a"
    elem = driver.find_element_by_tag_name(tag_name)
    print(elem.get_attribute("href"))

    xpath = "//*/following-sibling::a[1]"
    elem = driver.find_element_by_xpath(xpath)
    print(elem.get_attribute("href"))

    xpath = "//*/following-sibling::a[2]"
    elem = driver.find_element_by_xpath(xpath)
    print(elem.get_attribute("href"))

    xpath = "//*/following-sibling::div/a"
    elem = driver.find_element_by_xpath(xpath)
    print(elem.get_attribute("href"))

    xpath = "//*/following-sibling::div/a[2]"
    elem = driver.find_element_by_xpath(xpath)
    print(elem.get_attribute("href"))

    xpath = "//*/following-sibling::div/a[3]"
    elem = driver.find_element_by_xpath(xpath)
    print(elem.get_attribute("href"))

    xpath = "//*/following-sibling::div[2]/a"
    elem = driver.find_element_by_xpath(xpath)
    print(elem.get_attribute("href"))

    xpath = "//*/following-sibling::div[3]/a"
    elem = driver.find_element_by_xpath(xpath)
    print(elem.get_attribute("href"))

    xpath = "//*/following-sibling::div[4]/a"
    elem = driver.find_element_by_xpath(xpath)
    print(elem.get_attribute("href"))

if __name__ == "__main__":
    path = r"C:\Users\David\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(path)
    try:
        login(driver)
        scroll_photos(driver, "selfie")
    finally:
        print("that's all...")
    # driver.quit()

