import requests
from requests.exceptions import Timeout, HTTPError
import time
from parsel import Selector


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


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
