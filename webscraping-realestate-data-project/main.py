from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
import csv
import re

options = webdriver.ChromeOptions()
options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"


driver = webdriver.Chrome(options=options)


# ----- LISTING ID's -----
def get_ids(driver):
    element = driver.find_elements(By.CSS_SELECTOR, '.mb-srp__list')
    ids = [e.get_attribute('id') for e in element]
    return ids
# -------------------------------------------------



#  functions
def extract_info(driver, i):
    try:
        raw_description = driver.find_element(By.XPATH, f'//*[@id="{i}"]/div/div[1]/div[2]/div[4]/div').text
        description = re.sub(r'\s+', ' ', raw_description)

    except NoSuchElementException:
        description = "Null"
    try:
        raw_title = driver.find_element(By.XPATH, f'//*[@id="{i}"]/div/div[1]/div[2]/h2').text
        title = re.sub(r'\s+', ' ', raw_title)
    except NoSuchElementException:
        title = "Null"
    try:
        raw_price = driver.find_element(By.XPATH, f'//*[@id="{i}"]/div/div[2]/div[1]/div[1]').text
        price = re.sub(r'\s+', ' ', raw_price)
    except NoSuchElementException:
        price = "Null"
    try:
        raw_sq_ft_price = driver.find_element(By.XPATH, f'//*[@id="{i}"]/div/div[2]/div[1]/div[2]').text
        sq_ft_price = re.sub(r'\s+', ' ', raw_sq_ft_price)
    except NoSuchElementException:
        sq_ft_price = "Null"

    try:
        list_id = driver.find_element(By.XPATH, f'//*[@id="{i}"]')
        prop_list = list_id.find_element(By.CSS_SELECTOR, 'div.mb-srp__card__summary.open')
        prop_id = prop_list.get_attribute('id')
    except NoSuchElementException:
        try:
            prop_list = list_id.find_element(By.CSS_SELECTOR, 'div.mb-srp__card__summary')
            prop_id = prop_list.get_attribute('id')
        except NoSuchElementException:
            prop_id = None
    try:
        raw_summary = driver.find_element(By.XPATH, f'//*[@id="{prop_id}"]/div[1]').text
        summary = re.sub(r'\s+', ' ', raw_summary)
    except NoSuchElementException:
        summary = 'Null'

    return (i, title, description, price, sq_ft_price, summary)

def navigate_to_next_page(driver, page=0):
    try:
        next_page = driver.find_element(By.XPATH, '//*[@id="body"]/div[4]/div/div/div[1]/div[38]/ul/li[8]/a')
        next_page.click()
        time.sleep(5)

    except NoSuchElementException:
        print("Next page button not found")

    for i in range(1, page):
        time.sleep(5)
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")


def add_extract_info_into_data(driver, ids, data):
    for i in ids:
        info = extract_info(driver, i)
        data.append(info)
    return data


def scrape_data(driver, city, page=2):
    url = f'https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa,Residential-Plot&cityName={city}'
    driver.get(url)
    time.sleep(5)
    data = []
    ids = get_ids(driver)

    add_extract_info_into_data(driver, ids, data)

    navigate_to_next_page(driver, page)

    ids2 = get_ids(driver)

    add_extract_info_into_data(driver, ids2, data)

    with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Listing ID', 'Title', 'Description', 'Price', 'Sq Ft Price', 'Summary'])
        writer.writerows(data)


# Call the function
scrape_data(driver, city='mumbai', page=5)
