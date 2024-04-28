"""
functions are responsible for crawling from Magic bricks website
with provided configurations
"""

from bs4 import BeautifulSoup
import requests
import yaml
import json
import time
import traceback

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.helper import *
from src.transform import *

property_param_path = "config.yaml"

with open(property_param_path, 'r') as file:
    property_data = yaml.safe_load(file)


def get_property_urls() -> list:
    """
    using selenium and beautiful soup will extract the required number of property links

    input params None
    return List of Urls: list
    """
    firefox_options = Options()
    firefox_options.headless = True

    driver = webdriver.Firefox(options=firefox_options)

    url = str(
            "https://www.magicbricks.com/property-for-sale/residential-real-estate?&" + 
            f"cityName={property_data['params']['cityName']}&" +
            f"proptype={','.join(property_data['params']['proptype'])}&" +
            "category=S&mbTrackSrc=tabChange"
        )

    driver.get(url)
    
    list_urls, data_elements = [], []

    while True:
        # Scroll to the bottom of the page
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        # Get the page source after interactions
        page_source = driver.page_source
        # Parse the page source with Beautiful Soup
        soup = BeautifulSoup(page_source, "html.parser")
        # Extract data using Beautiful Soup methods
        data_elements = soup.find_all("div", class_="mb-srp__card has-package")
        if len(data_elements) >= property_data['params']["weblink_limit"]:
            break
        # Wait for a short time to allow content to load (adjust as needed)
        time.sleep(4)

    driver.quit()

    for ele in data_elements:
        script = ele.find("script")
        list_urls.append(json.loads(script.text.strip())["url"])
    return list_urls


def get_property_details(url: str) -> dict:
    """
    get the crawled content
    input params: url
    return crawled data: dict
    """
    try:
        response = requests.get(url)
        title_content = BeautifulSoup(response.content,  features="lxml").find("div", class_ = "mb-ldp__dtls__title--text1")
        details = BeautifulSoup(response.content, features="lxml").find("div", class_="mb-ldp__dtls__body")
        more_details = BeautifulSoup(response.content, features="lxml").find("div", class_="mb-ldp__more-dtl")

        property_summary_details = {
            "title": get_property_title(title_content),
            "link": url,
        }

        property_summary_details.update(get_property_details_part1(details))
        property_summary_details.update(get_property_details_part2(details))
        property_summary_details.update(get_property_details_part3(more_details))
    except Exception as e:
        print(url)
        traceback.print_exc()
        raise e
    return property_summary_details

