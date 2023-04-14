from tech_news.database import search_news


# Requisito 7
def search_by_title(title: str) -> list[tuple]:
    query = {"title": {"$regex": title, "$options": "i"}}
    matching_news = search_news(query)
    return [(news["title"], news["url"]) for news in matching_news]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
