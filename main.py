"""
Entry Point
"""

from src.data_extraction import *


urls = get_property_urls()

all_property_details = []

for url in urls:
    property_detail = get_property_details(url)
    property_detail = rm_unwanted_info(property_detail)
    all_property_details.append(property_detail)
    
def save_in_json_file(list_of_dicts: dict, file_path: str):
    """
    saving the data in json file
    :input params: list_of_dicts: crawled data
    :input params: file_path: file to save crawled data
    """
    with open(file_path, 'w', encoding="utf-8") as json_file:
        json.dump(list_of_dicts, json_file, indent=4, ensure_ascii=False)

save_in_json_file(all_property_details, file_path="indore_property_2.json")