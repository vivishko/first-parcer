import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd


def parse_top_kinopoisk():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.kinopoisk.ru/lists/movies/top250/")
    title = driver.title
    message = "not that page"
    link_message = driver.current_url
    assert title == "250 лучших фильмов — Кинопоиск", link_message
    df = pd.DataFrame({'Name': [], 'Link': []})
    # elems_names = driver.find_elements(By.CLASS_NAME, "desktop-list-main-info_secondaryText__M_aus")
    elems_links = driver.find_elements(By.CLASS_NAME, "base-movie-main-info_link__YwtP1")
    for i in range(len(elems_links)):
        # print(elems_names[i].text)
        print(elems_links[i].get_atribute("href"))
        # df = df.append({'Name': elems_names[i].text, 'Link': elems_links[i].get_atribute("href")}, ignore_index=True)
    # df.to_csv(r'C:\Projects\first-parser\1_top_elements.txt', header=None, index=None)
    driver.quit()


parse_top_kinopoisk()
