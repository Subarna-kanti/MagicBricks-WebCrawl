"""
functions will help to filtered and transformed the extracted data
"""

from src.helper import *

def get_property_title(soup):
    title_content = soup.find_all("span")
    title = title_content[0].text + ", " + title_content[1].text
    return title

def get_property_details_part1(soup):
    property_details = {}
    summary_cards = soup.\
                        find("ul", class_ = "mb-ldp__dtls__body__summary").\
                        find_all("li", class_ = "mb-ldp__dtls__body__summary--item")
    for content in  summary_cards:
        label = content.get("data-icon")
        value = content.find("span").text
        try:
            value = int(value)
        except ValueError:
            pass
        property_details[label] = value
    return property_details    

def get_property_details_part2(soup):
    property_details = {}
    summary_cards = soup.\
                        find("ul", class_ = "mb-ldp__dtls__body__list").\
                        find_all("li", class_ = "mb-ldp__dtls__body__list--item")
    for content in summary_cards:
        label = content.find("div", class_= "mb-ldp__dtls__body__list--label").text
        value = content.find("div", class_= "mb-ldp__dtls__body__list--value").text
        if label == "Carpet Area" or label == "Super Built-up Area":
            value = extract_price(str(content.find("div", class_= "mb-ldp__dtls__body__list--value")))
            unit = content.find("span", class_= "mb-ldp__dtls__body__list--units").find("span").text
            value = value + " " + unit
            rate = content.find("div", class_= "mb-ldp__dtls__body__list--size")
            if rate: rate = rate.text
            property_details["rate"] = rate
        property_details[label] = value
    return property_details

def get_property_details_part3(soup):
    property_details = {}
    more_detail_cards = soup.find("ul", class_ = "mb-ldp__more-dtl__list")              
    for content in more_detail_cards:
        label = content.find("div", class_= "mb-ldp__more-dtl__list--label").text
        value = content.find("div", class_= "mb-ldp__more-dtl__list--value").text
        property_details[label] = value
    description = soup.find("div", class_= "mb-ldp__more-dtl__description")
    if description:
        property_details["Description"] = description.find("span", class_ = "mb-ldp__more-dtl__description--content full hide").find("p").text
    return property_details