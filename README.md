# MagicBricks-WebCrawl
This repository is dedicated to crawling Magic Brick properties for specified locations utilizing frameworks such as Selenium, BeautifulSoup, and HTTP GET requests.

Objective:
    1. Fetch approximately 100 properties in Indore under various categories from Magic Bricks.
    2. Save the fetched data in a well-organized JSON file.

Approach:
    1. Create pipeline:
        a. Fetch/Crawl data from Magic Bricks.
        b. Transform the crawled data to the required dictionalry format.
        c. Repeat a and b for n number of properties.
        d. Create an array of all the property details and save it in a JSON file.
    2.  Crawling:
        a. Crawled website links using Selenium and Beautiful Soup.
        b. Saved the weblink urls in a list.
        c. Iterate through each link and crawl data of the respective property using GET request calls and Beautiful Soup.
        d. Transform each crawled data and save it in JSON.
    3. Transformation:
        a. Transform each crawled content to the desired JSON content.
        b. Extract the required content from the large chunk of data using features of Beautiful Soup.
        c. This feature is responsible for generating the final JSON file.
    4. Helper:
        An additional file to aid in crawling and transforming processes. This is an additional file, this helps our crawling and transforming.
    5. Config:
        Config file has been maintained to provide required configurations like:
            a. the number of properties
            b. city
            c. type of properties
    6. Filename:
        Currently, the file name is indore_property.json, as it includes all the indore properties.

Note:
    1. Please use the requirements.txt file to create a Python environment
    2. Python version == 3.11.9
    3. Install Mozilla Firefox to Selenium work for crawling
