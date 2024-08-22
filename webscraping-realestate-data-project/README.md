**Magic Bricks Data Scraper**
==========================

**Project Overview**
-------------------

This project involves web scraping real estate data from Magic Bricks, a popular Indian real estate portal. The scraper extracts valuable information such as property details, prices, locations, and more. I undertook this project to demonstrate my web scraping and data cleaning skills.

**Technologies Used**
--------------------

### Web Scraping

* Python
* Selenium
* Requests
* Beautiful Soup (initially used, but replaced by Selenium due to infinite scroll functionality)

### Data Cleaning

* Jupyter Notebook
* Pandas
* NumPy
* re (regular expressions)

**Features**
--------

* Extracts property details from Magic Bricks
* Handles pagination and scraping multiple pages
* Saves data to a CSV file
* Used error handling to make the script robust

**Reason for choosing Selenium over Beautiful Soup**
---------------------------------------------------

The website has an infinite scroll function, making it impossible to scrape all details using Beautiful Soup. Therefore, I used Selenium WebDriver to scroll and extract all the details.

**Usage**
-----

You can use this script to scrape Magic Bricks listing details for any city!

**Challenges Faced**
-------------------

* Extracting the property ID to get each listing's summary
* Error handling
* Data cleaning took significant time due to extracting insights from summary, description, and title

**Data Sample**
-------------

### Raw Data

| Listing ID | Title | Description | Price | Sq Ft Price | Summary |
| --- | --- | --- | --- | --- | --- |
| 71632357 | 2 BHK Apartment for Sale in Kelambakkam Chennai | ... | ₹ 39.9 Lac | ₹4,000 per sqft | ... |
| 73795355 | 2 BHK Builder Floor for Sale in Mudichur Chennai | ... | ₹ 50.6 Lac | ₹5,800 per sqft | ... |

### Cleaned Data

| listing_id | city | neighbourhood | property_type | total_sqft | no_of_rooms | furnish | sale_type | status | price | price (in 'k') | price_per_sqft |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 71632357 | Chennai | Kelambakkam | Apartment | 997 | 2 BHK | Unfurnished | New Property | Ready to Move | ₹ 39.9 Lac | 3990 | 4000 |
| 73795355 | Chennai | Mudichur | Builder Floor | 873 | 2 BHK | Under Construction | New Property | UNDER CONSTRUCTION | ₹ 50.6 Lac | 5060 | 5800 |

**Future Enhancements**
---------------------

* Applying ML to predict prices for 2030 in first-tier cities in India
* Explanatory analysis with the data to find insights

**Connect with me!**
-------------------

If you like my project, please give it a star! You can also connect with me on [LinkedIn](https://www.linkedin.com/in/maheshyoganandan/) to discuss more about this project or potential collaborations.

**Thank you!**
-------------

Thank you for visiting my project! The final output is a CSV file containing the cleaned and processed data, which I plan to share on Kaggle.
Let me know if you need any further modifications!
