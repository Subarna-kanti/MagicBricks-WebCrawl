"""
functions are responsible for helping
crawl and transform functionalities
"""

import re

def extract_price(html_content):
    pattern = r'>(\d+)<span'
    match = re.search(pattern, html_content)

    if match:
        return match.group(1)
    return None

def rm_unwanted_info(property_detail):
    rm_key = property_detail.get("Furnished Status")
    if rm_key:
        rm_key = rm_key.lower()
        property_detail.pop(rm_key, None)
    return property_detail
