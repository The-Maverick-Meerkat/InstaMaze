from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time # for delay
import re

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
    driver.find_element_by_partial_link_text("Load").click()

    code_str = ""

    tag_name = "a"
    pattern = "/p/"

    elem = driver.find_element_by_tag_name(tag_name)
    code_item = elem.get_attribute("href")
    if re.search(pattern, code_item):
        code_item = code_item.split("/p/")[1].split("/?")[0]
        code_str = code_str + code_item + "\n"

    i = 1
    counter = 1 # general counter of how many image-code we saved
    rows = 8   # the original page will have 8 rows (4 for latest + 4 after button
    cols = 2    # original row have only 2 siblings
    row_c = 1
    col_c = 1
    div = ""
    while(i < 2):
        while(row_c <= rows):
            while(col_c <= cols):
                xpath = "//*/following-sibling::" + div + "a[" + str(col_c) + "]"
                elem = driver.find_element_by_xpath(xpath)
                code_item = elem.get_attribute("href")
                if re.search(pattern, code_item):
                    code_item = code_item.split("/p/")[1].split("/?")[0]
                    print(code_item)
                    code_str = code_str + code_item + "\n"
                    counter += 1
                col_c += 1
            col_c = 1
            cols = 3
            row_c += 1
            div = "div[" + str(row_c - 1) +"]/"

        with open('codes.txt', 'a') as outfile:
            outfile.write(code_str)
        code_str = ""

        time.sleep(0.5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        row_c += 4
        i += 1
        # time.sleep(0.5)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(1)
        # driver.execute_script("window.scrollTo(0, 0);")
    print(counter)


if __name__ == "__main__":
    path = r"C:\Users\David\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(path)
    try:
        login(driver)
        scroll_photos(driver, "selfie")
    finally:
        print("that's all...")
    # driver.quit()

