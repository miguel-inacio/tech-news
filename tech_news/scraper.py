import requests
from requests.exceptions import Timeout, HTTPError
import time
from parsel import Selector
import re


# Requisito 1
def fetch(url: str) -> str:
    header = {"user-agent": "Fake user-agent"}
    try:
        time.sleep(1)
        response = requests.get(url, headers=header, timeout=3)
        response.raise_for_status()
        return response.text
    except (Timeout, HTTPError):
        return None


# Requisito 2
def scrape_updates(html_content: str) -> list[str]:
    selector = Selector(html_content)
    urls_list = []
    for card in selector.css("div.post-outer"):
        urls_list.append(card.css("a.cs-overlay-link::attr(href)").get())
    return urls_list if len(urls_list) > 0 else []


# Requisito 3
def scrape_next_page_link(html_content: str):
    selector = Selector(html_content)
    next_button = selector.css("a.next::attr(href)").get()
    return next_button


def ending_cleaning(string: str) -> str:
    repaired_string = string.split("\xa0")[0]
    if repaired_string.endswith(". "):
        return repaired_string[:-1]
    else:
        return repaired_string


# Função para remover tags html e fazer a limpeza da string
# Fonte =
# https://medium.com/@jorlugaqui/how-to-strip-html-tags-from-a-string-in-python-7cb81a2bbf44
def remove_html_tags(text):
    regex = re.compile("<.*?>")
    return re.sub(regex, "", text)


def get_number(reading_time: str) -> int:
    all_words = reading_time.split(" ")
    time = [int(char) for char in all_words if char.isdigit()]
    return int(time[0])


# Requisito 4
def scrape_news(html_content: str) -> dict:
    selector = Selector(html_content)
    url = ending_cleaning(
        selector.css("link[rel='canonical']::attr(href)").get()
    )
    title = selector.css("h1.entry-title::text").get()
    timestamp = selector.css("li.meta-date::text").get()
    author = selector.css("span.author > a::text").get()
    reading_time = selector.css("li.meta-reading-time::text").get()
    summary = remove_html_tags(
        selector.css("div.entry-content > p").getall()[0]
    )
    category = selector.css("a.category-style > span.label::text").get()

    return {
        "url": url,
        "title": ending_cleaning(title),
        "timestamp": timestamp,
        "writer": author,
        "reading_time": get_number(reading_time),
        "category": category,
        "summary": ending_cleaning(summary),
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
