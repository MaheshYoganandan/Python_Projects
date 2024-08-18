import requests
from bs4 import BeautifulSoup
import csv

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver


options = webdriver.ChromeOptions()
options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

driver = webdriver.Chrome(options=options)
actions = ActionChains(driver)


def scrape_imdb_movie_links(link, scroll=2):
    website_url = link
    driver.get(website_url)
    time.sleep(3)

    # Use ActionChains to move to the element and click it
    for i in range(1, scroll):
        more_movies = driver.find_element(By.CSS_SELECTOR,
                                          '#__next > main > div.ipc-page-content-container.ipc-page-content-container--center.sc-fb7106c2-0.eMsshF > div.ipc-page-content-container.ipc-page-content-container--center > section > section > div > section > section > div:nth-child(2) > div > section > div.ipc-page-grid.ipc-page-grid--bias-left.ipc-page-grid__item.ipc-page-grid__item--span-2 > div.ipc-page-grid__item.ipc-page-grid__item--span-2 > div.sc-619d2eab-0.dxnOGI > div > span > button')
        time.sleep(5)
        actions.move_to_element(more_movies).click().perform()

    time.sleep(10)

    movies = driver.find_elements(By.CSS_SELECTOR, "div.ipc-title a.ipc-title-link-wrapper")
    movie_links = [movie.get_attribute("href") for movie in movies]

    print(len(movie_links))

    driver.quit()

    return movie_links


def scrape_imdb_movie_details(movie_links):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    movie_records = []

    for url in movie_links:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        title_id = url.split('/')[-2]

        try:
            # movie title
            title = soup.find('span', class_='hero__primary-text', attrs={'data-testid': 'hero__primary-text'}).text
        except AttributeError:
            title = None

        try:
            year = soup.find('a', href=lambda h: 'releaseinfo' in h).text
        except AttributeError:
            year = None

        try:
            # director
            director = soup.find('a', class_='ipc-metadata-list-item__list-content-item--link').text
        except:
            director = None

        # runtime
        try:
            runtime = soup.find('li', string=lambda t: 'h' in t and t.lower().endswith('m')).text
        except AttributeError:
            runtime = None

        # rating
        try:
            rating = soup.find('span', class_='sc-eb51e184-1 ljxVSS').text
        except AttributeError:
            rating = None

        # vote
        try:
            vote = soup.find(class_='sc-eb51e184-3 kgbSIj').text
        except AttributeError:
            vote = None

        # parental guide
        try:
            parental_guide = soup.find('a', href=lambda h: 'parentalguide' in h).text
        except AttributeError:
            parental_guide = None

        # release date
        try:
            release_date_with_country = soup.find('a',
                                                  class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link',
                                                  attrs={'role': 'button',
                                                         'href': f'/title/{title_id}/releaseinfo?ref_=tt_dt_rdat'}).text
            release_date = release_date_with_country.split('(')
        except AttributeError:
            release_date = None

        # budget
        try:
            estimated_budget = soup.find('li', attrs={'data-testid': 'title-boxoffice-budget'}).find('span',
                                                                                                     class_='ipc-metadata-list-item__list-content-item').text
            budget = estimated_budget.split()[0]
        except AttributeError:
            budget = None

        # oscar
        try:
            oscar = soup.find('li', attrs={'data-testid': 'award_information'}).find('a',
                                                                                     class_='ipc-metadata-list-item__label ipc-metadata-list-item__label--link').text
        except AttributeError:
            oscar = 0

        # awards
        try:
            awards = soup.select_one(
                'li[data-testid="award_information"] .ipc-metadata-list-item__list-content-item').text
        except AttributeError:
            awards = 0

        data = (title, year, director, runtime, parental_guide, rating, vote, release_date, budget, oscar, awards)
        movie_records.append(data)

    return movie_records


def save_to_csv(movie_records):
    with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            ['Title', 'Year', 'Director', 'Runtime', 'Parental Guide', 'Rating', 'Vote', 'Release Date', 'Budget',
             'Oscar', 'Awards'])
        writer.writerows(movie_records)


url = 'https://www.imdb.com/search/title/?title_type=feature,tv_movie,tv_special,video&interests=in0000076'

# Scrape the movie links
movie_links = scrape_imdb_movie_links(url, scroll=40)

# Scrape the movie details
movie_records = scrape_imdb_movie_details(movie_links)

# Save the data to a CSV file
save_to_csv(movie_records)
