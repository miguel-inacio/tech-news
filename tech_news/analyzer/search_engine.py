from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title: str) -> list[tuple]:
    query = {"title": {"$regex": title, "$options": "i"}}
    matching_news = search_news(query)
    return [(news["title"], news["url"]) for news in matching_news]


# Requisito 8
def search_by_date(date: str) -> list[tuple]:
    try:
        fixed_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        query = {"timestamp": fixed_date}
        matching_dates = search_news(query)
        return [(news["title"], news["url"]) for news in matching_dates]

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
