import requests
from requests.exceptions import Timeout, HTTPError
import time


# Requisito 1
def fetch(url: str):
    header = {"user-agent": "Fake user-agent"}
    try:
        time.sleep(1)
        response = requests.get(url, headers=header, timeout=3)
        response.raise_for_status()
        return response.text
    except (Timeout, HTTPError):
        return None


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
