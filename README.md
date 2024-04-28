# MagicBricks-WebCrawl

This repository is dedicated to crawling Magic Brick properties for specified locations utilizing frameworks such as Selenium, BeautifulSoup, and HTTP GET requests.

## Objective

1. Fetch approximately 100 properties in Indore under various categories from Magic Bricks.
2. Save the fetched data in a well-organized JSON file.

## Approach

1. **Pipeline Creation**: 
    - Fetch/Crawl data from Magic Bricks.
    - Transform the crawled data to the required dictionary format.
    - Repeat steps a and b for n number of properties.
    - Create an array of all the property details and save it in a JSON file.

2. **Crawling**:
    - Crawled website links using Selenium and BeautifulSoup.
    - Saved the web link URLs in a list.
    - Iterate through each link and crawl data of the respective property using GET request calls and BeautifulSoup.
    - Transform each crawled data and save it in JSON.

3. **Transformation**:
    - Transform each crawled content to the desired JSON content.
    - Extract the required content from the large chunk of data using features of BeautifulSoup.
    - This feature is responsible for generating the final JSON file.

4. **Helper**:
    - An additional file to aid in crawling and transforming processes.

5. **Config**:
    - Configuration file to provide required configurations like:
        - the number of properties
        - City
        - the type of properties

6. **Filename**:
    - Currently, the file name is indore_property.json, as it includes all the Indore properties.

## Notes

1. Please use the `requirements.txt` file to create a Python environment.
2. Python version == 3.11.9.
3. Install Mozilla Firefox for Selenium to work for crawling.

## Getting Started

To get started with this project, follow these steps:

1. Clone this repository to your local machine.
2. Create a Python environment using the `requirements.txt` file.
3. Install Mozilla Firefox.
4. Execute the Python scripts to crawl MagicBricks properties for the specified location.

Feel free to contribute or provide feedback to improve this project!
