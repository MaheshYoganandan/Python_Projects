# IMDb Movie Data Scraper


## Portfolio Project

This project is a part of my portfolio to showcase my skills in web scraping, data cleaning, and data analysis.

## Project Description

This project involves web scraping of movie data from IMDb using Selenium and Beautiful Soup. The data is then cleaned and stored in a CSV file using Jupyter Notebook, NumPy, and Pandas.

## Tools Used

* **Selenium**: Used for automating web browser interactions to scroll through IMDb pages and collect movie links.
* **Beautiful Soup**: Used for parsing HTML and extracting movie details from individual movie pages.
* **Requests**: Used for making HTTP requests to IMDb pages.
* **Python**: Used as the programming language for the entire project.
* **Jupyter Notebook**: Used for data cleaning and preprocessing using NumPy and Pandas.
* **NumPy** and **Pandas**: Used for data manipulation and analysis.

## Process

### Data Collection

* Used Selenium to automate web browser interactions and click "Show More" buttons to load more movies on IMDb pages.
* Collected links of individual movie pages and stored them in a list.

### Data Extraction

* Used Beautiful Soup to extract movie details from individual movie pages.
* Extracted details include:
	+ Title
	+ Director
	+ Runtime
	+ Parental Guide
	+ Awards
	+ Year
	+ Released Date
	+ Oscar nominations and wins
	+ BAFTA nominations and wins
	+ Emmy nominations and wins

### Error Handling

* Implemented error handling to avoid:
	+ `NoSuchElementException`
	+ `AttributeError`
	+ Other errors that may occur during web scraping
* Used try-except blocks to catch and handle errors, ensuring the script runs smoothly and doesn't stop unexpectedly

### Data Cleaning

* Used Jupyter Notebook for data cleaning and preprocessing.
* Imported necessary libraries: NumPy and Pandas.
* Cleaned and processed data to obtain the following columns:
	+ Title
	+ Director
	+ Runtime
	+ Parental Guide
	+ Awards
	+ Year
	+ Released Date
	+ Oscar nominations
	+ Oscar won
	+ BAFTA won
	+ BAFTA nomination
	+ Emmy won
	+ Emmy nomination

## Output

The final output is a CSV file containing the cleaned and processed movie data.

## Project Stats

* Extracted data from **1900+** movies from IMDb website.
* After cleaning and preprocessing, **1300+** data points were obtained.

## Scalability

This code can be used to extract more than **100000+** movies data by simply adjusting the parameters and running the script for an extended period.

## Support

If you like my project, please give it a star! You can also connect with me on [LinkedIn](link_to_your_linkedin_profile) to discuss more about this project or potential collaborations.

Thank you for visiting my project!
