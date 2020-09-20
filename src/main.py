
import os
import time

from browser import Browser
from gmapsurl import GMapsURL
from gmapsnav import GMapsNav

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.chrome.options import Options

CHROMEDRIVER_PATH = os.environ['CHROMEDRIVER_PATH']
CHROME_OPTIONS = webdriver.ChromeOptions() #Options()
CHROME_OPTIONS.add_argument("--user-data-dir=.\chrome-data")
CHROME_OPTIONS.add_argument("--enable-automation")

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=CHROME_OPTIONS)
GMAPS_URL = 'https://www.google.com/maps/'

if __name__ == '__main__':

    # examples of search and place strings
    search_str = 'petrolina pizzaria'
    spot_str = 'Pizzaria Jecana'

    # GMapsNav instatiation
    gmaps = GMapsNav(driver, GMAPS_URL)

    # uses search string to get a list of places strings
    spots_str = gmaps.get_spots_str(search_str)
    print(spots_str)
    time.sleep(5)

    # uses search string and a place string to get a dict about the place
    #gmaps.get_spot(search_str, spot_str)
    #time.sleep(10)

    driver.quit()