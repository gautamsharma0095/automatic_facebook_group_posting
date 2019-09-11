# -*- coding: utf-8 -*-
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    # Your Facebook account user and password
    usr = ""
    pwd = ""

    message = "Let's change the way our world is powered \nhttp://www.electricalidea.com/solar-panel/ \n #solarpanelsystem #solarenergypanels #pánelessolares #solarpanelsuppliers #solarpaneled #solarpanelwashing #panelessolares #solarpanelsinsonipat #panelessolaresrd #solarpanel #canadiansolarpanels #panelessolarespty #flexiblesolarpanels #panelesolares #solarpanels #solarpanelsfordays #solarpanelinstaller #solarpanelslasvegas #solarpanelinstallation #solarpanelcleaners #solarpanelsinstallation #panelsolar #panelessolarestrace #solarpanelsperth #jualsolarpanel #solarpanelcleaning #solarpanelcleaner #solarpanelroof #panelsolarpanama #solarpanelmurah"
    # set multiple fb groups here
    df = pd.read_excel("Facebooks.xlsx")
    group_links = df["URL"].tolist()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.notifications": 2  # 1:allow, 2:block
    })
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options, executable_path=r'C:\selenium driver\chromedriver.exe')
    driver.implicitly_wait(15)  # seconds

    # Go to facebook.com
    driver.get("http://www.facebook.com")

    # Enter user email
    elem = driver.find_element_by_id("email")
    elem.send_keys(usr)
    # Enter user password
    elem = driver.find_element_by_id("pass")
    elem.send_keys(pwd)
    # Login
    elem.send_keys(Keys.RETURN)

    for group in group_links:
        try:
            # Go to the Facebook Group
            driver.get(group)

            # Click the post box
            post_box = driver.find_element_by_xpath("//*[@name='xhpc_message_text']")

            # Enter the text we want to post to Facebook
            post_box.send_keys(message)

            sleep(5)
            try:
                post = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button/span[.="Post"]')))
                post.click()
            except StaleElementReferenceException as e:
                raise e
            sleep(5)
        except Exception as e:
            print("URL IS: {}", format(group))
            print("Error: {}", format(e))

    print("All Groups Posting Finished")
    driver.close()


if __name__ == '__main__':

    main()
