# Python Projects
## Ecommerce Dataset Exploratory Data Analysis (EDA) [Link](https://github.com/MaheshYoganandan/Python_Projects/tree/main/python-retail-data-analysis-project)

### Project Overview

Exploratory data analysis on an ecommerce dataset to gain insights, identify patterns, and visualize findings using various visualization libraries.

### Technologies Used

* Python
* Pandas
* NumPy
* Seaborn
* Matplotlib
* Plotly

### Key Findings

* Customer demographics, purchase history, and product details analysis
* Identified correlations and relationships between variables
* Conducted hypothesis testing and confidence intervals for significant findings

### Insights

* Consumer age group analysis
* Country-wise analysis
* Gender classification
* Income distribution analysis
* Customer segmentation

### Snaps
![retail_data_analysis_snap](https://github.com/user-attachments/assets/8ab54801-f537-40b1-a38d-cc1c434eb255)
![retail_data_analysis_snap](https://github.com/user-attachments/assets/e4022ceb-1578-42b5-8634-ec1d49026c8a)
![retail_data_analysis_snap](https://github.com/user-attachments/assets/4f2f73a4-4326-4025-948c-15e4a181de4e)
![retail_data_analysis_snap](https://github.com/user-attachments/assets/b397e1dc-63fb-43ed-9174-e91c85f9491b)



## IMDb Movie Data Scraper [Link](https://github.com/MaheshYoganandan/Python_Projects/tree/main/webscraping-imdb-movie-data-scraper-project)

### Project Description

Web scraping of movie data from IMDb using Selenium and Beautiful Soup, followed by data cleaning and storage in a CSV file.

### Tools Used

* Selenium
* Beautiful Soup
* Requests
* Python
* Jupyter Notebook
* NumPy and Pandas

### Process

* Data collection using Selenium
* Data extraction using Beautiful Soup
* Error handling and data cleaning using Jupyter Notebook and NumPy and Pandas

### Output

A CSV file containing the cleaned and processed movie data.

### Project Stats

* Extracted data from **1900+** movies
* **1300+** data points obtained after cleaning and preprocessing

### Scalability

Can be used to extract more than **100000+** movies data by adjusting parameters and running the script for an extended period.

### Snaps
Raw Data
![raw_data](https://github.com/user-attachments/assets/658b6ccb-8e19-4bf4-9c0b-a4f0d63af4d7)

Cleaned Data
![cleaned_data](https://github.com/user-attachments/assets/361c18be-f8bd-4a69-823f-115ee3db4620)


## Magic Bricks Data Scraper [Link](https://github.com/MaheshYoganandan/Python_Projects/blob/main/webscraping-realestate-data-project/README.md?plain=1)

### Project Overview

This project involves web scraping real estate data from Magic Bricks, a popular Indian real estate portal. The scraper extracts valuable information such as property details, prices, locations, and more. I undertook this project to demonstrate my web scraping and data cleaning skills.

### Technologies Used

#### Web Scraping

* Python
* Selenium
* Requests
* Beautiful Soup (initially used, but replaced by Selenium due to infinite scroll functionality)

#### Data Cleaning

* Jupyter Notebook
* Pandas
* NumPy
* re (regular expressions)

### Features

* Extracts property details from Magic Bricks
* Handles pagination and scraping multiple pages
* Saves data to a CSV file
* Used error handling to make the script robust

### Reason for choosing Selenium over Beautiful Soup

The website has an infinite scroll function, making it impossible to scrape all details using Beautiful Soup. Therefore, I used Selenium WebDriver to scroll and extract all the details.

### Usage

You can use this script to scrape Magic Bricks listing details for any city!

### Challenges Faced

* Extracting the property ID to get each listing's summary
* Error handling
* Data cleaning took significant time due to extracting insights from summary, description, and title

### Snaps
Raw Data
![raw_data](https://github.com/user-attachments/assets/c6c04186-d965-4f84-b6af-c3c258292c6c)

Cleaned Data
![cleaned_data](https://github.com/user-attachments/assets/50d4a1ca-a545-40e0-8e63-75bcfae3fcdf)
