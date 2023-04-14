from tech_news.database import search_news
from collections import Counter

# Fontes:
# https://www.pythontutorial.net/python-basics/python-sort-list/
# https://stackoverflow.com/questions/69933073/how-to-sort-a-tuple-using-two-parameters


# Requisito 10
def top_5_categories():
    all_news = search_news({})
    all_categories = [news["category"] for news in all_news]
    counted_categories = Counter(all_categories)
    most_common_categories = counted_categories.most_common(5)
    sorted_categories = sorted(
        most_common_categories,
        key=lambda category: (-category[1], category[0]),
    )
    return [category[0] for category in sorted_categories]
