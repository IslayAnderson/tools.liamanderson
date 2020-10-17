import xml.etree.cElementTree as x2j
import json
import sys
import time
#import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

URL = 'https://www.google.com/search?q=liamanderson.co.uk'

javascript2 = "var style=\".google h3{color:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) h3\")).getPropertyValue(\"color\")+\";font-size:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) h3\")).getPropertyValue(\"font-size\")+\";font-weight:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) h3\")).getPropertyValue(\"font-weight\")+\";line-heigt:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) h3\")).getPropertyValue(\"line-heigt\")+\";padding-top:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) h3\")).getPropertyValue(\"padding-top\")+\";padding-bottom:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) h3\")).getPropertyValue(\"padding-bottom\")+\";padding-left:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) h3\")).getPropertyValue(\"padding-left\")+\";padding-right:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) h3\")).getPropertyValue(\"padding-right\")+\";margin-top:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) h3\")).getPropertyValue(\"margin-top\")+\";margin-bottom:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) h3\")).getPropertyValue(\"margin-bottom\")+\";margin-left:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) h3\")).getPropertyValue(\"margin-left\")+\";margin-right:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) h3\")).getPropertyValue(\"margin-right\")+\";}.google cite{color:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) cite\")).getPropertyValue(\"color\")+\";font-size:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) cite\")).getPropertyValue(\"font-size\")+\";line-weight:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) cite\")).getPropertyValue(\"font-weight\")+\";line-heigt:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) cite\")).getPropertyValue(\"line-heigt\")+\";padding-top:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) cite\")).getPropertyValue(\"padding-top\")+\";padding-bottom:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) cite\")).getPropertyValue(\"padding-bottom\")+\";padding-left:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) cite\")).getPropertyValue(\"padding-left\")+\";padding-right:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) cite\")).getPropertyValue(\"padding-right\")+\";margin-top:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) cite\")).getPropertyValue(\"margin-top\")+\";margin-bottom:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) cite\")).getPropertyValue(\"margin-bottom\")+\";margin-left:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) cite\")).getPropertyValue(\"margin-left\")+\";margin-right:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) cite\")).getPropertyValue(\"margin-right\")+\";}.google .d{color:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) div > div > span > span\")).getPropertyValue(\"color\")+\";font-weight:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) div > div > span > span\")).getPropertyValue(\"font-weight\")+\";font-height:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) div > div > span > span\")).getPropertyValue(\"line-heigt\")+\";font-size:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) div > div > span > span\")).getPropertyValue(\"font-size\")+\";padding-top:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) div > div > span > span\")).getPropertyValue(\"padding-top\")+\";padding-bottom:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) div > div > span > span\")).getPropertyValue(\"padding-bottom\")+\";padding-left:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) div > div > span > span\")).getPropertyValue(\"padding-left\")+\";padding-right:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) div > div > span > span\")).getPropertyValue(\"padding-right\")+\";margin-top:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) div > div > span > span\")).getPropertyValue(\"margin-top\")+\";margin-bottom:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) div > div > span > span\")).getPropertyValue(\"margin-bottom\")+\";margin-left:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) div > div > span > span\")).getPropertyValue(\"margin-left\")+\";margin-right:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) div > div > span > span\")).getPropertyValue(\"margin-right\")+\";height:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) div > div\")).getPropertyValue(\"height\")+\";}.google em{color:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) em\")).getPropertyValue(\"color\")+\";font-size:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) em\")).getPropertyValue(\"font-size\")+\";font-weight:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) em\")).getPropertyValue(\"font-weight\")+\";line-heigt:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) em\")).getPropertyValue(\"line-heigt\")+\";padding-top:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) em\")).getPropertyValue(\"padding-top\")+\";padding-bottom:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) em\")).getPropertyValue(\"padding-bottom\")+\";padding-left:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) em\")).getPropertyValue(\"padding-left\")+\";padding-right:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) em\")).getPropertyValue(\"padding-right\")+\";margin-top:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) em\")).getPropertyValue(\"margin-top\")+\";margin-bottom:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) em\")).getPropertyValue(\"margin-bottom\")+\";margin-left:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) em\")).getPropertyValue(\"margin-left\")+\";margin-right:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) em\")).getPropertyValue(\"margin-right\")+\";}.google{width:\"+getComputedStyle(document.querySelector(\"#rso > div:nth-child(1) div > div\")).getPropertyValue(\"width\")+\";}\";return style;"

scrape = []
results = ""
final = ""

options = Options()

options.headless = True

driver = webdriver.Firefox(options=options, executable_path = r'/var/www/vhosts/onlyrams.co.uk/httpdocs/data/geckodriver')

#driver = webdriver.Firefox()
driver.implicitly_wait(2)

driver.get(URL)

scrape.append(driver.execute_script(javascript2))
print("==============================")
print(scrape)
print("==============================")

with open("/var/www/vhosts/liamanderson.co.uk/tools.liamandersoon.co.uk/google.css", "w", encoding="utf-8") as file:
        file.write(str(scrape[0]))

driver.quit()
